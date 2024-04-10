from django.urls import path

from clients.views import (
    ClientListView,
    ClientCreateView,
    ClientDeleteView,
    ClientDetailsView,
    ClientUpdateView,
)

app_name = "clients"

urlpatterns = [
    # path("", shop_index, name="index"),

    # path("api/", include(routers.urls)),

    path("", ClientListView.as_view(), name="client_list"),
    path("create/", ClientCreateView.as_view(), name="client_create"),
    path("<int:pk>/", ClientDetailsView.as_view(), name="client_details"),
    path("<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("<int:pk>/archived/", ClientDeleteView.as_view(), name="client_archived"),
]
