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

from .forms import ContractForm
from .models import Contract
from .serializers import ContractSerializers
from utils import HasRolePermission


class ContractListView(PermissionRequiredMixin, ListView):
    permission_required = "contracts.view_contract"
    queryset = Contract.objects.all()


class ContractDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = "contracts.view_contract"
    model = Contract
    queryset = Contract.objects.all()


class ContractCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "contracts.add_contract"
    model = Contract
    form_class = ContractForm
    success_url = reverse_lazy("contracts:contract_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "contracts.change_contract"

    model = Contract
    form_class = ContractForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="contracts:contract_details",
            kwargs={"pk": self.object.pk},
        )


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "contracts.delete_contract"
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