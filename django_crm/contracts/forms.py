from django import forms
from django.forms import ModelForm

from .models import Contract


class DateInput(forms.DateInput):
    input_type = 'date'


class ContractForm(ModelForm):

    class Meta:
        model = Contract
        fields = "name", "service", "document_file", "date_conclusion", "period_validity", "amount",
        widgets = {
            'date_conclusion': DateInput(),
        }
