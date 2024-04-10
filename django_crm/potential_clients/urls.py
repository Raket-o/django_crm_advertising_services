from django.urls import path

from potential_client.views import (
    AdvertisingCompaniesListView,
    AdvertisingCompanyCreateView,
    AdvertisingCompanyDeleteView,
    AdvertisingCompanyDetailsView,
    AdvertisingCompanyUpdateView,
)

app_name = "customers"

urlpatterns = [
    # path("", shop_index, name="index"),

    # path("api/", include(routers.urls)),

    path("", AdvertisingCompaniesListView.as_view(), name="customers_list"),
    path("create/", AdvertisingCompanyCreateView.as_view(), name="customer_create"),
    path("<int:pk>/", AdvertisingCompanyDetailsView.as_view(), name="customer_company_details"),
    path("<int:pk>/update/", AdvertisingCompanyUpdateView.as_view(), name="customer_company_update"),
    path("<int:pk>/archived/", AdvertisingCompanyDeleteView.as_view(), name="customer_company_archived"),
]
