from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import PermissionsMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Client
from .serializers import ClientSerializers, ClientActiveSerializers, ClientToActiveSerializer
from utils import HasRolePermission


class ClientListView(PermissionRequiredMixin, ListView):
    permission_required = "clients.view_client"
    queryset = (
        Client.objects
        .prefetch_related("advertising_company")
        .filter(active=False)
    )


class ClientDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = "clients.view_client"
    model = Client
    queryset = (
        Client.objects
        .prefetch_related("advertising_company")
        .all()
    )


class ClientCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "clients.add_client"
    model = Client
    fields = "name", "phone", "email", "advertising_company",

    def get_success_url(self):
        return reverse(
            viewname="clients:client_details",
            kwargs={"pk": self.object.pk},
        )


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "clients.change_client"
    model = Client
    fields = "name", "phone", "email", "advertising_company",
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="clients:client_details",
            kwargs={"pk": self.object.pk},
        )


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "clients.delete_client"
    model = Client
    success_url = reverse_lazy("clients:client_list")


class ClientToActiveUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "clients.to_active_client"

    template_name = "clients/client_to_active.html"
    model = Client
    fields = "contract",
    success_url = reverse_lazy("clients:client_active_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.active = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ClientActiveListView(PermissionRequiredMixin, ListView):
    permission_required = "clients.view_active_client"
    template_name = "clients/client_active_list.html"
    queryset = (
        Client.objects
        .prefetch_related("advertising_company")
        .filter(active=True)
    )


class ClientActiveDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = "clients.view_active_client"
    template_name = "clients/client_active_detail.html"
    model = Client

    queryset = (
        Client.objects
        .select_related("contract")
        .prefetch_related("advertising_company")
        .all()
    )


class ClientActiveUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "clients.change_active_client"
    template_name = "clients/client_active_update_form.html"
    model = Client
    fields = "name", "phone", "email", "contract", "advertising_company",

    def get_success_url(self):
        return reverse(
            viewname="clients:client_active_details",
            kwargs={"pk": self.object.pk},
        )


class ClientActiveDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "clients.delete_active_client"
    template_name = "clients/client_confirm_active.html"
    model = Client
    success_url = reverse_lazy("clients:client_active_list")


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (HasRolePermission("operator"),)
    queryset = Client.objects.filter(active=False)
    serializer_class = ClientSerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    fields = [
        "name",
        "phone",
        "email",
        "advertising_company",
    ]

    search_fields = fields
    filterset_fields = fields
    ordering_fields = fields


class ClientActiveViewSet(viewsets.ModelViewSet):
    permission_classes = (HasRolePermission("manager"),)
    queryset = Client.objects.filter(active=True)
    serializer_class = ClientActiveSerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    fields = [
        "name",
        "phone",
        "email",
        "advertising_company",
        "contract",
    ]

    search_fields = fields
    filterset_fields = fields
    ordering_fields = fields

    def create(self, request, *args, **kwargs):
        return Response({'error': 'Запись запрещена'}, status=status.HTTP_403_FORBIDDEN)


class ClientToActiveViewSet(viewsets.ModelViewSet):
    permission_classes = (HasRolePermission("manager"),)
    queryset = Client.objects.filter(active=False)
    serializer_class = ClientToActiveSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    fields = [
        "name",
        "phone",
        "email",
        "advertising_company",
    ]

    search_fields = fields
    filterset_fields = fields
    ordering_fields = fields

    def create(self, request, *args, **kwargs):
        return Response({'error': 'The method is not available'}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.active = True

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return Response({'error': 'The method is not available'}, status=status.HTTP_403_FORBIDDEN)
