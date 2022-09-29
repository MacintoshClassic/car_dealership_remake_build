from rest_framework import serializers
from .models import Car, Client, Receipt


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "brand", "model", "year", "hp", "color", "price", "type")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "mail", "phone", "first_name", "second_name")


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("id", "car_id", "client_id")
