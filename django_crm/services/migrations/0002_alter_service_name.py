# Generated by Django 5.0.4 on 2024-04-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]