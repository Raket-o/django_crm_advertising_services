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

from .models import AdvertisingCompany
from .serializers import AdvertisingCompanySerializers
from utils import HasRolePermission


ROLE = "marketing"


class AdvertisingCompaniesListView(UserPassesTestMixin, ListView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    permission_required = "advertising_companies.view_advertisingcompany"
    template_name = "advertising_companies/advertising_companies_list.html"
    queryset = (
        AdvertisingCompany.objects
        .prefetch_related("services")
        .all()
    )


class AdvertisingCompanyDetailsView(UserPassesTestMixin, DetailView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    template_name = "advertising_companies/advertising_company_details.html"
    model = AdvertisingCompany
    queryset = (
        AdvertisingCompany.objects
        .prefetch_related("services")
        .all()
    )


class AdvertisingCompanyCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    template_name = "advertising_companies/advertising_company_form.html"
    model = AdvertisingCompany
    fields = "name", "description",  "promotion", "services", "budget",
    success_url = reverse_lazy("advertising_companies:advertising_companies_list")


class AdvertisingCompanyUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    template_name = "advertising_companies/advertising_company_update_form.html"
    model = AdvertisingCompany
    fields = "name", "description",  "promotion", "services", "budget",
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="advertising_companies:advertising_company_details",
            kwargs={"pk": self.object.pk},
        )


class AdvertisingCompanyDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    template_name = "advertising_companies/advertising_company_confirm_delete.html"
    model = AdvertisingCompany
    success_url = reverse_lazy("advertising_companies:advertising_companies_list")


class AdvertisingCompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (HasRolePermission("marketing"),)
    queryset = AdvertisingCompany.objects.all()
    serializer_class = AdvertisingCompanySerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    fields = [
        "name",
        "description",
        "promotion",
        "budget",
        "services",
    ]

    search_fields = fields
    filterset_fields = fields
    ordering_fields = fields
