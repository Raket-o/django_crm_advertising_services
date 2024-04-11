from django.urls import path

from .views import (
    ContractListView,
    ContractCreateView,
    ContractDeleteView,
    ContractDetailsView,
    ContractUpdateView,
)

app_name = "contracts"

urlpatterns = [
    # path("", shop_index, name="index"),

    # path("api/", include(routers.urls)),


    path("", ContractListView.as_view(), name="contract_list"),
    path("create/", ContractCreateView.as_view(), name="contract_create"),
    path("<int:pk>/", ContractDetailsView.as_view(), name="contract_details"),
    path("<int:pk>/update/", ContractUpdateView.as_view(), name="contract_update"),
    path("<int:pk>/delete/", ContractDeleteView.as_view(), name="contract_archived"),
]
