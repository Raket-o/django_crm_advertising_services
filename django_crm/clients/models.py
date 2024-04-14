from django.db import models

# Create your models here.

from advertising_companies.models import AdvertisingCompany
from contracts.models import Contract


class Client(models.Model):
    class Meta:
        verbose_name = "Potential client"
        verbose_name_plural = "Potential clients"
        ordering = "id", "name"

    name = models.CharField(max_length=50, blank=False, unique=True)
    phone = models.CharField(max_length=10, blank=False)
    email = models.EmailField(blank=True)
    active = models.BooleanField(default=False)
    advertising_company = models.ForeignKey(AdvertisingCompany, on_delete=models.CASCADE, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, default=None)

    # def __repr__(self):
    #     return (f"'advertising_company': {self.advertising_company}, 'contract': {self.contract}")

    def to_json(self):
        return (f"'advertising_company': {self.advertising_company}, 'contract': {self.contract}")

    # def __str__(self):
    #     return (f"'advertising_company': {self.advertising_company}, 'contract': {self.contract}")
