from django.db import models

# Create your models here.

from services.models import Service


# class AdvertisingCompany(models.Model):
#     class Meta:
#         verbose_name = "Advertising company"
#         verbose_name_plural = "Advertising companies"
#         ordering = "id", "name"
#
#     # name = models.CharField(max_length=50, blank=False)
#     # description = models.TextField(max_length=300, blank=True)
#     # promotion = models.TextField(max_length=50, blank=True)
#     # budget = models.DecimalField(max_digits=8, decimal_places=2, blank=True, default=0)
#     # services = models.One(Service, related_name="advertisingcompany")
#
#     name = models.CharField(max_length=50, blank=False)
#
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#
