from django.urls import path
from . import views
from .views import car, client, receipt

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "car/add/<str:brand>/<str:model>/<str:year>/<str:hp>/<str:color>/<str:price>/<str:type>",
        views.add_car,
        name="add_car",
    ),
    path(
        "client/add/<str:mail>/<str:phone>/<str:first_name>/<str:second_name",
        views.add_client,
        name="add_client",
    ),
    path("cheap_cars", views.get_cheap_cars, name="get_cheap_cars"),
    path("sports_cars", views.get_sports_cars, name="get_sports_cars"),
    path("trucks", views.get_trucks, name="get_trucks"),
    path("suvs", views.get_suvs, name="get_suvs"),
    path(
        "military_vehicles", views.get_military_vehicles, name="get_military_vehicles"
    ),
    path("retro_cars", views.get_retro_cars, name="get_retro_cars"),
    path("buy_car/<str:car_id>", views.buy_car, name="buy_car"),
    path(
        "buy_car_adding_to_db", views.buy_car_adding_to_db, name="buy_car_adding_to_db"
    ),
    path("order_information", views.order_information, name="order_information"),
    path(
        "order_information_printing_out",
        views.order_information_printing_out,
        name="order_information_printing_out",
    ),
    path(
        "add_client_who_doesnt_exist",
        views.add_client_who_doesnt_exist,
        name="add_client_who_doesnt_exist",
    ),
    path(
        "db_add_client_who_doesnt_exist",
        views.db_add_client_who_doesnt_exist,
        name="db_add_client_who_doesnt_exist",
    ),
    path("get_client_info", views.get_client_info, name="get_client_info"),
    path("client_added_approved", views.get_client_info, name="get_client_info"),
    path("car/", car, name="car"),
    path("client/", client, name="client"),
    path("receipt/", receipt, name="receipt"),
]
