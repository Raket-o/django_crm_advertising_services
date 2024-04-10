from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.core.cache import cache
from django.http import JsonResponse, Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

from .models import AdvertisingCompany
from .forms import AdvertisingCompanyForm


class AdvertisingCompaniesListView(ListView):
    template_name = "advertising_companies/advertising_companies_list.html"
    # queryset = AdvertisingCompany.objects.filter(archived=False)
    queryset = (
        AdvertisingCompany.objects
        .prefetch_related("services")
        .all()
    )


class AdvertisingCompanyDetailsView(DetailView):
    template_name = "advertising_companies/advertising_company_details.html"
    model = AdvertisingCompany
    # queryset = AdvertisingCompany.objects.filter(archived=False)

    queryset = (
        AdvertisingCompany.objects
        .prefetch_related("services")
        .all()
    )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     for obj in self.queryset:
    #         total_price = sum(obj.get_service_price())
    #
    #     # total_price = sum(tuple(obj.get_service_price() for obj in self.queryset))
    #     context['total_price'] = total_price
    #     return context


# class ServiceCreateView(PermissionRequiredMixin, CreateView):
class AdvertisingCompanyCreateView(CreateView):
    # permission_required = "services.add_service"
    template_name = "advertising_companies/advertising_company_form.html"
    model = AdvertisingCompany
    # fields = "name", "description", "services", "promotion"
    form_class = AdvertisingCompanyForm
    # success_url = reverse_lazy("advertising_companies:advertising_companies_list")

    def form_valid(self, form):
        AdvertisingCompany.set_budget(form)
        # response = super().form_valid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            viewname="advertising_companies:advertising_company_details",
            kwargs={"pk": self.object.pk},
        )


# class ServiceUpdateView(UserPassesTestMixin, UpdateView):
class AdvertisingCompanyUpdateView(UpdateView):
    template_name = "advertising_companies/advertising_company_update_form.html"
    model = AdvertisingCompany
    # fields = "name", "description", "services", "promotion",
    # template_name_suffix = "_update_form"
    form_class = AdvertisingCompanyForm

    # def test_func(self):
    #     user = self.request.user
    #     product = get_object_or_404(Product, pk=self.kwargs["pk"])
    #     return user.is_superuser or user.has_perm("shopapp.change_product") or product.created_by.pk == user.pk

    def get_success_url(self):
        return reverse(
            viewname="advertising_companies:advertising_company_details",
            kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        AdvertisingCompany.set_budget(form)
        # response = super().form_valid(form)
        return super().form_valid(form)


# class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
class AdvertisingCompanyDeleteView(DeleteView):
    # permission_required = "services.delete_service"
    template_name = "advertising_companies/advertising_company_confirm_delete.html"
    model = AdvertisingCompany
    success_url = reverse_lazy("advertising_companies:advertising_companies_list")

    # def form_valid(self, form):
    #     success_url = self.get_success_url()
    #     # self.object.archived = True
    #     self.object.delete()
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)
