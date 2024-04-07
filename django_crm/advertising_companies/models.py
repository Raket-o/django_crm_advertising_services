from django.db import models

from services.models import Service


class AdvertisingCompany(models.Model):
    class Meta:
        verbose_name = "Advertising company"
        verbose_name_plural = "Advertising companies"

    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    services = models.ManyToManyField(Service, related_name="advertisingcompany")
    archived = models.BooleanField(default=False)
