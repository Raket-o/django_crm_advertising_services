from django.urls import path

from .views import (
    AdvertisingCompaniesListView,
    AdvertisingCompanyCreateView,
    AdvertisingCompanyDeleteView,
    AdvertisingCompanyDetailsView,
    AdvertisingCompanyUpdateView,
)

app_name = "advertising_companies"

urlpatterns = [
    # path("", shop_index, name="index"),

    # path("api/", include(routers.urls)),

    path("", AdvertisingCompaniesListView.as_view(), name="advertising_companies_list"),
    path("create/", AdvertisingCompanyCreateView.as_view(), name="advertising_company_create"),
    path("<int:pk>/", AdvertisingCompanyDetailsView.as_view(), name="advertising_company_details"),
    path("<int:pk>/update/", AdvertisingCompanyUpdateView.as_view(), name="advertising_company_update"),
    path("<int:pk>/archived/", AdvertisingCompanyDeleteView.as_view(), name="advertising_company_archived"),
]