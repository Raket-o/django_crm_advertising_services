from django.urls import path

from .views import CustomerStatistics

app_name = "customer_statistics"

urlpatterns = [
    path("", CustomerStatistics.as_view(), name="statistics"),
]
