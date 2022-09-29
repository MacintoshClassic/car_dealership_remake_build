from calendar import c
from msilib.schema import Error
from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, Client, Receipt
from .forms import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer, ClientSerializer, ReceiptSerializer


def index(request):
    return render(request, "myapp/index.html", {})


def add_car(request, brand, model, year, hp, color, price, type):
    car = Car(
        brand=brand,
        model=model,
        year=year,
        hp=hp,
        color=color,
        price=price,
        type=type,
    )
    car.save()
    return HttpResponse("car was added to the database")


def add_client(request, mail, phone, first_name, second_name):
    client = Client(
        mail=mail,
        phone=phone,
        first_name=first_name,
        second_name=second_name,
    )
    client.save()
    return HttpResponse("client was added to the database")


def get_cheap_cars(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        if car.type == "cheap":
            car_list.append(car)
    context = {"car_list": car_list}
    return render(request, "myapp/cheap_cars.html", context)


def get_sports_cars(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        if car.type == "sports":
            car_list.append(car)
    context = {"car_list": car_list}
    return render(request, "myapp/sports_cars.html", context)


def get_trucks(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        if car.type == "truck":
            car_list.append(car)
    context = {"car_list": car_list}
    return render(request, "myapp/trucks.html", context)


def get_suvs(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        if car.type == "suv":
            car_list.append(car)
    context = {"car_list": car_list}
    return render(request, "myapp/suvs.html", context)


def get_military_vehicles(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        if car.type == "military":
            car_list.append(car)
    context = {"car_list": car_list}
    return render(request, "myapp/military_vehicles.html", context)


def get_retro_cars(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        if car.type == "retro":
            car_list.append(car)
    context = {"car_list": car_list}
    return render(request, "myapp/retro_cars.html", context)


# https://docs.djangoproject.com/en/4.1/ref/forms/fields/
# тут мы вписываем дефолтное значение car_id, то, которое идет после buy_car/
def buy_car(request, car_id):
    form = BuyCar({"car_id": car_id})
    context = {"form": form}
    return render(request, "myapp/buy_car.html", context)


# buy_car --> buy_car_adding_to_db
def buy_car_adding_to_db(request):
    client_id = request.GET["client_id"]
    client = Client.objects.get(pk=client_id)
    car_id = request.GET["car_id"]
    car = Car.objects.get(pk=car_id)
    receipt = Receipt(
        car_id=car,
        client_id=client,
    )
    receipt.save()
    return render(request, "myapp/car_was_purchased.html", {})


def order_information(request):
    form = OrerInformation()
    context = {"form": form}
    return render(request, "myapp/order_info.html", context)


# order_information --> order_information_printing_out
def order_information_printing_out(request):
    client_id = request.GET["client_id"]
    receipts = Receipt.objects.filter(client_id=client_id)
    car_list = []
    for receipt in receipts:
        car_list.append(receipt.car_id)
    if Client.objects.filter(pk=client_id).exists():
        if Receipt.objects.filter(client_id=client_id).exists():
            if len(car_list) > 0:
                context = {"car_list": car_list}
                return render(
                    request, "myapp/order_information_printing_out.html", context
                )
            else:
                pass
        else:
            return render(request, "myapp/you_have_no_purchase(s).html", {})
    else:
        return render(request, "myapp/add_client_who_doesnt_exist.html", {})


def add_client_who_doesnt_exist(request):
    return render(request, "myapp/add_client_who_doesnt_exist.html", {})


def db_add_client_who_doesnt_exist(request):
    form = AddClientWhoDoesntExist()
    context = {"form": form}
    return render(request, "myapp/db_add_client_who_doesnt_exist.html", context)


def get_client_info(request):
    mail = request.GET["mail"]
    phone = request.GET["phone"]
    first_name = request.GET["first_name"]
    second_name = request.GET["second_name"]

    client = Client(
        mail=mail,
        phone=phone,
        first_name=first_name,
        second_name=second_name,
    )
    client.save()
    return render(request, "myapp/client_added_approved.html", {})


@api_view(["GET", "POST"])
def car(request):
    if request.method == "GET":  # user requesting data
        snippets = Car.objects.all()
        serializer = CarSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":  # user posting data
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def client(request):
    if request.method == "GET":
        snippets = Client.objects.all()
        serializer = ClientSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def receipt(request):
    if request.method == "GET":
        snippets = Receipt.objects.all()
        serializer = ReceiptSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
