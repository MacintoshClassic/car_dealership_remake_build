from socket import fromshare
from django import forms


class BuyCar(forms.Form):
    client_id = forms.CharField(label="Input client id:", max_length=100)
    car_id = forms.CharField(label="Input car id:", max_length=100)


class OrerInformation(forms.Form):
    client_id = forms.CharField(label="Input client id:", max_length=100)


class AddClientWhoDoesntExist(forms.Form):
    mail = forms.CharField(label="Type client mail:", max_length=100)
    phone = forms.CharField(label="Type client phone:", max_length=100)
    first_name = forms.CharField(label="Type client first name:", max_length=100)
    second_name = forms.CharField(label="Type client second name:", max_length=100)
