from django.urls import path
# from django.urls import include, path
# from rest_framework.routers import DefaultRouter

from .views import (
    AdvertisingCompaniesListView,
    AdvertisingCompanyCreateView,
    AdvertisingCompanyDeleteView,
    AdvertisingCompanyDetailsView,
    AdvertisingCompanyUpdateView,
    AdvertisingCompanyViewSet,
)

app_name = "advertising_companies"

# routers = DefaultRouter()
# routers.register("advertising_companies", AdvertisingCompanyViewSet, basename='advertising_companies')

urlpatterns = [
    path("", AdvertisingCompaniesListView.as_view(), name="advertising_companies_list"),
    path("create/", AdvertisingCompanyCreateView.as_view(), name="advertising_company_create"),
    path("<int:pk>/", AdvertisingCompanyDetailsView.as_view(), name="advertising_company_details"),
    path("<int:pk>/update/", AdvertisingCompanyUpdateView.as_view(), name="advertising_company_update"),
    path("<int:pk>/delete/", AdvertisingCompanyDeleteView.as_view(), name="advertising_company_archived"),

    # path("", include(routers.urls)),

]
