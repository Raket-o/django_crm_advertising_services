# Generated by Django 5.0.4 on 2024-04-15 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
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
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "document_file",
                    models.FileField(null=True, upload_to="contracts/contracts/"),
                ),
                ("date_conclusion", models.DateTimeField()),
                ("period_validity", models.CharField(max_length=50)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="names",
                        to="services.service",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contract",
                "verbose_name_plural": "Contracts",
                "ordering": ("id", "name"),
            },
        ),
    ]
