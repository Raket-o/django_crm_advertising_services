from django.urls import path

from .views import (
    ServicesListView,
    ServiceCreateView,
    ServiceDeleteView,
    ServiceDetailsView,
    ServiceUpdateView,
)

app_name = "services"

urlpatterns = [
    # path("", shop_index, name="index"),

    # path("api/", include(routers.urls)),


    path("", ServicesListView.as_view(), name="service_list"),
    path("create/", ServiceCreateView.as_view(), name="service_create"),
    path("<int:pk>/", ServiceDetailsView.as_view(), name="service_details"),
    path("<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"),
    path("<int:pk>/archived/", ServiceDeleteView.as_view(), name="service_archived"),
]
