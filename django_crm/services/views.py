from django.shortcuts import render

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

from .models import Service


class ServicesListView(ListView):
    template_name = "services/services_list.html"
    queryset = Service.objects.filter(archived=False)


class ServiceDetailsView(DetailView):
    template_name = "services/service_details.html"
    model = Service
    queryset = Service.objects.filter(archived=False)


# class ServiceCreateView(PermissionRequiredMixin, CreateView):
class ServiceCreateView(CreateView):
    # permission_required = "services.add_service"

    model = Service
    fields = "name", "description"
    success_url = reverse_lazy("services:services_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


# class ServiceUpdateView(UserPassesTestMixin, UpdateView):
class ServiceUpdateView(UpdateView):
    model = Service
    fields = "name", "description",
    template_name_suffix = "_update_form"

    # def test_func(self):
    #     user = self.request.user
    #     product = get_object_or_404(Product, pk=self.kwargs["pk"])
    #     return user.is_superuser or user.has_perm("shopapp.change_product") or product.created_by.pk == user.pk

    def get_success_url(self):
        return reverse(
            viewname="services:service_details",
            kwargs={"pk": self.object.pk},
        )


# class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
class ServiceDeleteView(DeleteView):
    # permission_required = "services.delete_service"

    model = Service
    success_url = reverse_lazy("services:services_list")

    # def form_valid(self, form):
    #     success_url = self.get_success_url()
    #     # self.object.archived = True
    #     self.object.delete()
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)