from .models import Contract
from rest_framework import serializers


class ContractSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
