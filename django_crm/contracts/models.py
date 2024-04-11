from django.db import models

from services.models import Service


class Contract(models.Model):
    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"
        ordering = "id", "name"

    name = models.CharField(max_length=50, blank=False, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="names")
    document_file = models.FileField(null=True, upload_to='contracts/contracts/')
    date_conclusion = models.DateTimeField()
    period_validity = models.CharField(max_length=50, blank=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=False)


    # def __repr__(self):
    #     return str(self.price)

    # def __str__(self):
    #     return f"Name: {self.name}, price: {self.price}"
