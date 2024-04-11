# from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django.forms import ModelForm, DateTimeField

from django import forms


from .models import Contract


class DateInput(forms.DateInput):
    input_type = 'date'


class ContractForm(ModelForm):

    class Meta:
        model = Contract

        fields = "name", "service", "document_file", "date_conclusion", "period_validity", "amount",

        # widgets = {
        #     'date_conclusion': DatePickerInput(),
        # }

        widgets = {
            'date_conclusion': DateInput(),
        }

        # date_conclusion = DateTimeField(widget=DateInput(format='%Y-%m-%d'),
        #                                 input_formats=('%Y-%m-%d',),
        #                                 required=False)
