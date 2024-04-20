from django.db import models

from services.models import Service


class AdvertisingCompany(models.Model):
    class Meta:
        verbose_name = "Advertising company"
        verbose_name_plural = "Advertising companies"
        ordering = "id", "name"

    name = models.CharField(max_length=50, unique=True, blank=False)
    description = models.TextField(max_length=300, blank=True)
    promotion = models.CharField(max_length=50, blank=False)
    budget = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __repr__(self):
        return (f"'id': {self.id}, 'name':{self.name}, 'budget': {self.budget}, 'services_price': {self.services.__repr__()}")

    def __str__(self):
        return self.name
