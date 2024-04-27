from django.contrib.auth.mixins import PermissionRequiredMixin
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


class ServicesListView(PermissionRequiredMixin, ListView):
    permission_required = "services.view_service"
    queryset = Service.objects.all()


class ServiceDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = "services.view_service"
    model = Service
    queryset = Service.objects.all()


class ServiceCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "services.add_service"
    model = Service
    fields = "name", "description", "price"
    success_url = reverse_lazy("services:service_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class ServiceUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "services.change_service"

    model = Service
    fields = "name", "description", "price"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="services:service_details",
            kwargs={"pk": self.object.pk},
        )


class ServiceDeleteView(DeleteView):
    permission_required = "services.delete_service"
    model = Service
    success_url = reverse_lazy("services:service_list")


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = [
        "name",
        "description",
        "price",
    ]
    filterset_fields = [
        "name",
        "description",
        "price",
    ]
    ordering_fields = [
        "id",
        "name",
        "price",
    ]
