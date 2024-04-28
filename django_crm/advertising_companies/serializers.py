from .models import AdvertisingCompany
from rest_framework import serializers


class AdvertisingCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingCompany
        fields = '__all__'
