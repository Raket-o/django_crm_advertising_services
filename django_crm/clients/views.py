from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.core.cache import cache
from django.http import JsonResponse, Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views import View
from django.urls import reverse_lazy

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
    # form_class = AdvertisingCompanyForm
    # success_url = reverse_lazy("advertising_companies:advertising_companies_list")

    # def form_valid(self, form):
    #     AdvertisingCompany.set_budget(form)
    #     # response = super().form_valid(form)
    #     return super().form_valid(form)

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
    permission_required = "clients.delete_active_clients"
    template_name = "clients/client_confirm_delete.html"
    model = Client
    success_url = reverse_lazy("clients:client_active_list")

