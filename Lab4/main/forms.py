from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import inlineformset_factory

from main.models import Hotel, Country, Order, Ticket, Client


# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'inputbox-input'}))
#     password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'inputbox-input', 'style': 'top: 55%;'}))

# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'inputbox', 'placeholder': 'Login'}))
#     password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'inputbox', 'placeholder': 'Password'}))

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'TextInput'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'TextInput'}))


class RegisterUserForm(UserCreationForm):
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'TextInput'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'TextInput'}))
    patronymic = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'TextInput'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'TextInput'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'TextInput'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'TextInput'}))


class HotelDetailForm:
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'': 'TextInput'}))


class AddHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "stars", "cost_per_day", "country"]


class AddCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["name", "climate_spring", "climate_summer", "climate_autumn", "climate_winter"]


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["last_name", "first_name", "patronymic", "email", "phone_number", "date"]


# OrderClientFormSet = inlineformset_factory(Order, Client, form=AddClientForm, extra=1)


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["tickets", "departure_date", "discount"]


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["name", "hotels", "duration", "price"]


class EditHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "stars", "cost_per_day", "country"]

