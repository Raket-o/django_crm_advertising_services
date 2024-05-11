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

from .forms import ContractForm
from .models import Contract
from .serializers import ContractSerializers
from utils import HasRolePermission


ROLE = "manager"


class ContractListView(UserPassesTestMixin, ListView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    queryset = Contract.objects.all()


class ContractDetailsView(UserPassesTestMixin, DetailView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    permission_required = "contracts.view_contract"
    model = Contract
    queryset = Contract.objects.all()


class ContractCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    model = Contract
    form_class = ContractForm
    success_url = reverse_lazy("contracts:contract_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class ContractUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    model = Contract
    form_class = ContractForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="contracts:contract_details",
            kwargs={"pk": self.object.pk},
        )


class ContractDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        user = self.request.user
        groups = set(str(group) for group in user.groups.all())
        if ROLE in groups or user.is_staff:
            return True

    model = Contract
    success_url = reverse_lazy("contracts:contract_list")


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = (HasRolePermission("manager"),)
    queryset = Contract.objects.all()
    serializer_class = ContractSerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    fields = [
        "name",
        "service",
        "date_conclusion",
        "period_validity",
        "amount",
    ]

    search_fields = fields
    filterset_fields = fields
    ordering_fields = fields