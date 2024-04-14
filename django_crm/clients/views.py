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

# Create your views here.

from .models import Client
# from .forms import AdvertisingCompanyForm


class ClientListView(ListView):
    # template_name = "clients/clients_list.html"
    # queryset = AdvertisingCompany.objects.filter(archived=False)
    queryset = (
        Client.objects
        .prefetch_related("advertising_company")
        .filter(active=False)
    )


class ClientDetailsView(DetailView):
    # template_name = "clients/client_details.html"
    model = Client
    # queryset = AdvertisingCompany.objects.filter(archived=False)

    queryset = (
        Client.objects
        .prefetch_related("advertising_company")
        .all()
    )

    # queryset = (
    #     Client.objects
    #     .all()
    # )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     for obj in self.queryset:
    #         total_price = sum(obj.get_service_price())
    #
    #     # total_price = sum(tuple(obj.get_service_price() for obj in self.queryset))
    #     context['total_price'] = total_price
    #     return context


# class ServiceCreateView(PermissionRequiredMixin, CreateView):
class ClientCreateView(CreateView):
    # permission_required = "services.add_service"
    # template_name = "clients/client_form.html"
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


# class ServiceUpdateView(UserPassesTestMixin, UpdateView):
class ClientUpdateView(UpdateView):
    # template_name = "clients/client_update_form.html"
    model = Client
    fields = "name", "phone", "email", "advertising_company",
    template_name_suffix = "_update_form"
    # form_class = AdvertisingCompanyForm

    # def test_func(self):
    #     user = self.request.user
    #     product = get_object_or_404(Product, pk=self.kwargs["pk"])
    #     return user.is_superuser or user.has_perm("shopapp.change_product") or product.created_by.pk == user.pk

    def get_success_url(self):
        return reverse(
            viewname="clients:client_details",
            kwargs={"pk": self.object.pk},
        )

    # def form_valid(self, form):
    #     AdvertisingCompany.set_budget(form)
    #     # response = super().form_valid(form)
    #     return super().form_valid(form)


# class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
class ClientDeleteView(DeleteView):
    # permission_required = "services.delete_service"
    # template_name = "clients/client_confirm_delete.html"
    model = Client

    if model.contract:
        success_url = reverse_lazy("clients:client_active_list")
    else:
        success_url = reverse_lazy("clients:client_list")


    # def form_valid(self, form):
    #     success_url = self.get_success_url()
    #     # self.object.archived = True
    #     self.object.delete()
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)


class ClientToActiveUpdateView(UpdateView):
    # permission_required = "services.delete_service"
    template_name = "clients/client_to_active.html"
    model = Client
    fields = "contract",
    success_url = reverse_lazy("clients:client_active_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.active = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ClientActiveListView(ListView):
    template_name = "clients/client_active_list.html"
    queryset = (
        Client.objects
        .prefetch_related("advertising_company")
        .filter(active=True)
    )


class ClientActiveDetailsView(DetailView):
    template_name = "clients/client_active_detail.html"
    model = Client

    queryset = (
        Client.objects
        .select_related("contract")
        .prefetch_related("advertising_company")
        .all()
    )


class ClientActiveUpdateView(UpdateView):
    template_name = "clients/client_active_update_form.html"
    model = Client
    fields = "name", "phone", "email", "contract", "advertising_company",

    # def test_func(self):
    #     user = self.request.user
    #     product = get_object_or_404(Product, pk=self.kwargs["pk"])
    #     return user.is_superuser or user.has_perm("shopapp.change_product") or product.created_by.pk == user.pk

    def get_success_url(self):
        return reverse(
            viewname="clients:client_active_details",
            kwargs={"pk": self.object.pk},
        )
