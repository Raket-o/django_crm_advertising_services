# Generated by Django 5.0.4 on 2024-04-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("advertising_companies", "0003_alter_advertisingcompany_budget"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advertisingcompany",
            name="budget",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=8
            ),
        ),
        migrations.AlterField(
            model_name="advertisingcompany",
            name="promotion",
            field=models.TextField(blank=True, max_length=50),
        ),
    ]