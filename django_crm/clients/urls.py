from django.urls import path

from clients.views import (
    ClientListView,
    ClientCreateView,
    ClientDeleteView,
    ClientDetailsView,
    ClientUpdateView,
    ClientToActiveUpdateView,
    ClientActiveListView,
    ClientActiveDetailsView,
    ClientActiveUpdateView,
    ClientActiveDeleteView,
)

app_name = "clients"

urlpatterns = [
    path("", ClientListView.as_view(), name="client_list"),
    path("create/", ClientCreateView.as_view(), name="client_create"),
    path("<int:pk>/", ClientDetailsView.as_view(), name="client_details"),
    path("<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("<int:pk>/archived/", ClientDeleteView.as_view(), name="client_archived"),

    path("<int:pk>/client-to-active/", ClientToActiveUpdateView.as_view(), name="client_to_active"),
    path("active/", ClientActiveListView.as_view(), name="client_active_list"),
    path("active/<int:pk>/", ClientActiveDetailsView.as_view(), name="client_active_details"),
    path("active/<int:pk>/update/", ClientActiveUpdateView.as_view(), name="client_active_update"),
    path("active/<int:pk>/archived/", ClientActiveDeleteView.as_view(), name="client_active_archived"),

]
