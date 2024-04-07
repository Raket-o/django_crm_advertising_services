# Generated by Django 5.0.4 on 2024-04-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvertisingCompany",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=50)),
                ("description", models.TextField(blank=True, max_length=300)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("archived", models.BooleanField(default=False)),
                (
                    "services",
                    models.ManyToManyField(
                        related_name="advertisingcompany", to="services.service"
                    ),
                ),
            ],
            options={
                "verbose_name": "Advertising company",
                "verbose_name_plural": "Advertising companies",
            },
        ),
    ]