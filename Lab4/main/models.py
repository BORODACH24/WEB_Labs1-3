from django.db import models

from promocodes.models import PromoCode


# Create your models here.


class Client(models.Model):
    last_name = models.CharField('Last name', max_length=50)
    first_name = models.CharField('First name', max_length=50)
    patronymic = models.CharField('Patronymic', max_length=50)
    email = models.EmailField('Email', max_length=50)
    phone_number = models.CharField('Phone number', max_length=50, default="+666(66)666-66-66")
    date = models.CharField('Date', max_length=50, default="1111-11-11")


class Country(models.Model):
    name = models.CharField(max_length=50)
    climate_spring = models.CharField(max_length=100)
    climate_summer = models.CharField(max_length=100)
    climate_autumn = models.CharField(max_length=100)
    climate_winter = models.CharField(max_length=100)
    pass


class Employee(models.Model):
    pass


class Hotel(models.Model):
    name = models.CharField('Name', max_length=50)
    stars = models.IntegerField('Stars', choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])
    cost_per_day = models.FloatField('Cost per day')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    pass


class Ticket(models.Model):
    '''
    куда
    дата
    на какое кол-во человек
    '''
    name = models.CharField(max_length=100)
    # countries = models.ManyToManyField(Country)
    hotels = models.ManyToManyField(Hotel)
    duration = models.IntegerField(choices=[(1, '1 week'), (2, '2 weeks'), (3, '3 weeks'), (4, '4 weeks')])
    price = models.FloatField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    departure_date = models.DateField()
    discount = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True)

