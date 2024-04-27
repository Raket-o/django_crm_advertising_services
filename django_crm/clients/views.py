from django.contrib.auth.mixins import PermissionRequiredMixin
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
