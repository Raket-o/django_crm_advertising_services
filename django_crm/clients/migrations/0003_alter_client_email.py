# Generated by Django 5.0.4 on 2024-04-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0002_client_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
