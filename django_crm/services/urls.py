from django.urls import path
from django.views.decorators.cache import cache_page
from django_crm.settings import CACHE_SECONDS

from .views import (
    ServiceCreateView,
    ServiceDeleteView,
    ServiceDetailsView,
    ServicesListView,
    ServiceUpdateView,
)

app_name = "services"

urlpatterns = [
    path("", ServicesListView.as_view(), name="service_list"),
    path("create/", ServiceCreateView.as_view(), name="service_create"),
    path("<int:pk>/", cache_page(CACHE_SECONDS)(ServiceDetailsView.as_view()), name="service_details"),
    path("<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"),
    path("<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_archived"),
]
