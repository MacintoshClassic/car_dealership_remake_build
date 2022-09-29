from django.conf import settings
from django.db import models
from django.forms import IntegerField


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    hp = models.IntegerField()
    color = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=100)


class Client(models.Model):
    mail = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)


class Receipt(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
