from django.urls import path

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
    path("<int:pk>/", ServiceDetailsView.as_view(), name="service_details"),
    path("<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"),
    path("<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_archived"),
]
