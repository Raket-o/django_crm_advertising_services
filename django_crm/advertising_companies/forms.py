from django import forms

from .models import AdvertisingCompany

from django.db import models


class AdvertisingCompanyForm(forms.ModelForm):
    class Meta:
        model = AdvertisingCompany
        service_checkbox = "services"
        fields = "name", "description", "promotion", service_checkbox

        widgets = {
            service_checkbox: forms.CheckboxSelectMultiple(),
        }
