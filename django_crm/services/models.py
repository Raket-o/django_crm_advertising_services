from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = "id", "name"

    name = models.TextField(max_length=50, unique=True, blank=False)
    description = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # def __repr__(self):
    #     return str(self.price)

    def __str__(self):
        return f"Name: {self.name}, price: {self.price}"
