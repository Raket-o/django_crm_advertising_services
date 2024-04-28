from .models import Client
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
        fields = '__all__'

        # fields = [
        #     "id",
        #     "active",
        #     "contract",
        # ]
        # fields = [
        #     "id",
        #     "name",
        #     "phone",
        #     "email",
        #     "advertising_company",
        #     "active",
        #     "contract",
        # ]

        # field1 = serializers.CharField(read_only=True)
        # id = serializers.IntegerField(read_only=True)
        # name = serializers.CharField(read_only=True)

        field1 = serializers.IntegerField(read_only=True)
        field2 = serializers.CharField(read_only=True)

# надо чтоб нельзя было создавать, но детально редактировать можно
