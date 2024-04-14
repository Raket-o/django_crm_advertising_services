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
    # services = models.ManyToManyField(Service, related_name="advertisingcompany")
    # services = models.ManyToManyField(Service, through='AdvertisingcompanyServicesMTM')
    services = models.ForeignKey(Service, on_delete=models.CASCADE)

    # def get_service_price(self):
    #     return tuple((int(service.price) for service in self.services.all()))
    #
    # @classmethod
    # def set_budget(cls, form):
    #     total_price_services = sum(tuple(service.price for service in form.cleaned_data['services']))
    #     project = form.save(commit=False)
    #     project.budget = total_price_services
    #     project.save()
    #     return project

    def __str__(self):
        return self.name


# class AdvertisingcompanyServicesMTM(models.Model):
#     advertisingcompany_id = models.ForeignKey(AdvertisingCompany, on_delete=models.CASCADE)
#     service_id = models.ForeignKey(Service, on_delete=models.PROTECT)


