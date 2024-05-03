from .models import Client
from contracts.models import Contract
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "advertising_company",
        ]


class ClientActiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "advertising_company",
            "contract",
        ]


class ClientToActiveSerializer(serializers.ModelSerializer):
    queryset = Contract.objects.all()
    name = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    advertising_company = serializers.CharField(read_only=True)
    contract = serializers.PrimaryKeyRelatedField(queryset=queryset, required=True)

    class Meta:
        model = Client

        fields = [
            "id",
            "name",
            "phone",
            "email",
            "advertising_company",
            "contract",
        ]
