from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.core.cache import cache
from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import AdvertisingCompany


class AdvertisingCompaniesListView(PermissionRequiredMixin, ListView):
    permission_required = "advertising_companies.view_advertisingcompany"
    template_name = "advertising_companies/advertising_companies_list.html"
    queryset = (
        AdvertisingCompany.objects
        .prefetch_related("services")
        .all()
    )


class AdvertisingCompanyDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = "advertising_companies.view_advertisingcompany"
    template_name = "advertising_companies/advertising_company_details.html"
    model = AdvertisingCompany
    queryset = (
        AdvertisingCompany.objects
        .prefetch_related("services")
        .all()
    )


class AdvertisingCompanyCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "advertising_companies.add_advertisingcompany"
    template_name = "advertising_companies/advertising_company_form.html"
    model = AdvertisingCompany
    fields = "name", "description",  "promotion", "services", "budget",
    success_url = reverse_lazy("advertising_companies:advertising_companies_list")


class AdvertisingCompanyUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "advertising_companies.change_advertisingcompany"
    template_name = "advertising_companies/advertising_company_update_form.html"
    model = AdvertisingCompany
    fields = "name", "description",  "promotion", "services", "budget",
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="advertising_companies:advertising_company_details",
            kwargs={"pk": self.object.pk},
        )


class AdvertisingCompanyDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "advertising_companies.delete_advertisingcompany"
    template_name = "advertising_companies/advertising_company_confirm_delete.html"
    model = AdvertisingCompany
    success_url = reverse_lazy("advertising_companies:advertising_companies_list")
