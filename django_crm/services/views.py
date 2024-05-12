from django.contrib.auth.mixins import UserPassesTestMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Service
from .serializers import ServiceSerializers
from utils import HasRolePermission


ROLE = "marketing"


class ServicesListView(UserPassesTestMixin, ListView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    queryset = Service.objects.all()


class ServiceDetailsView(UserPassesTestMixin, DetailView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    model = Service
    queryset = Service.objects.all()


class ServiceCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    model = Service
    fields = "name", "description", "price"
    success_url = reverse_lazy("services:service_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class ServiceUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    model = Service
    fields = "name", "description", "price"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="services:service_details",
            kwargs={"pk": self.object.pk},
        )


class ServiceDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    model = Service
    success_url = reverse_lazy("services:service_list")


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (HasRolePermission("marketing"),)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    fields = [
        "name",
        "description",
        "price",
    ]

    search_fields = fields
    filterset_fields = fields
    ordering_fields = fields
