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

from .models import Service


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
