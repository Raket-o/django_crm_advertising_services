from django.urls import path
from django.views.decorators.cache import cache_page
from django_crm.settings import CACHE_SECONDS

from .views import CustomerStatistics

app_name = "customer_statistics"

urlpatterns = [
    path("", cache_page(CACHE_SECONDS)(CustomerStatistics.as_view()), name="statistics"),
]
