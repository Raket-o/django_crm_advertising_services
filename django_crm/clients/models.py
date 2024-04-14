from django.db import models

# Create your models here.

from advertising_companies.models import AdvertisingCompany
from contracts.models import Contract


class Client(models.Model):
    class Meta:
        verbose_name = "Potential client"
        verbose_name_plural = "Potential clients"
        ordering = "id", "name"

    # name = models.CharField(max_length=50, blank=False)
    # description = models.TextField(max_length=300, blank=True)
    # promotion = models.TextField(max_length=50, blank=True)
    # budget = models.DecimalField(max_digits=8, decimal_places=2, blank=True, default=0)
    # services = models.One(Service, related_name="advertisingcompany")

    name = models.CharField(max_length=50, blank=False, unique=True)
    phone = models.CharField(max_length=10, blank=False)
    email = models.EmailField(blank=True)
    active = models.BooleanField(default=False)
    advertising_company = models.ForeignKey(AdvertisingCompany, on_delete=models.CASCADE, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, default=None)


