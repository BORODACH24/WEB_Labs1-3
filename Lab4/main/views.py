from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView
import requests
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from main.forms import LoginUserForm, RegisterUserForm, AddHotelForm, AddCountryForm, AddClientForm, AddOrderForm, \
    AddTicketForm
from main.models import Hotel, Ticket, Country, Client, Order
from news.models import Newsletter
from promocodes.models import PromoCode


def is_store_owner(user):
    return user.is_superuser or user.is_authenticated and user.has_perm('your_app.can_access_store_owner_views')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return '/'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    # form_class = UserCreationForm
    template_name = 'main/signup.html'

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')


def privacy_policy_view(request):
    return render(request, 'main/Privacy_Policy.html')


def contacts_view(request):
    return render(request, 'main/Contacts.html')


def about_us_view(request):
    return render(request, 'main/AboutUs.html')


def home_view(request):
    api_url_1 = 'https://official-joke-api.appspot.com/random_joke'  # Replace with your API endpoint URL
    api_url_2 = 'https://catfact.ninja/fact'  # Replace with your API endpoint URL

    # Make a GET request
    # response_1 = requests.get(api_url_1)
    response_2 = requests.get(api_url_2)

    # if response_1.status_code == 200:
    #     # Process the response data
    #     data = response_1.json()
    #
    #     # ...
    # else:
    #     # Handle the error response
    #     error_message = response_1.text
    data = {
        'setup': 'Test',
        'punchline': 'test',
    }
    if response_2.status_code == 200:
        # Process the response data

        cats = response_2.json()
        # ...
    else:
        # Handle the error response
        error_message = response_2.text

    newsletter = Newsletter.objects.latest('id')
    return render(request, 'main/MainPage.html', {'data': data, 'cats': cats, "newsletter": newsletter})


def hotel_list(request):
    search_query = request.GET.get('search_query', '')
    sort_by = request.GET.get('sort_by', 'name')
    hotels = Hotel.objects.all()

    if search_query:
        hotels = hotels.filter(
            Q(name__icontains=search_query) |
            Q(stars__icontains=search_query)
        )

    if sort_by == 'name':
        hotels = hotels.order_by('name')
    elif sort_by == 'stars':
        hotels = hotels.order_by('stars')
    elif sort_by == 'cost_per_day':
        hotels = hotels.order_by('cost_per_day')

    context = {
        'request': request,
        'hotels': hotels,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, "main/hotel_list.html", context)
    # Implement any additional filtering or sorting logic based on user input
    # return render(request, 'main/hotel_list.html', {'hotels': hotels})


def search_hotels(request):
    search_query = request.GET.get('q')

    hotels = Hotel.objects.filter(Q(name__icontains=search_query) | Q(stars__icontains=search_query))
    # Add more conditions for other sorting options as needed
    # ...

    return render(request, 'main/hotel_list.html', {'hotels': hotels})


@login_required
def add_hotel(request):
    countries = Country.objects.all()
    if request.method == 'POST':
        form = AddHotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
        else:
            return render(request, 'main/add_hotel.html', {'form': form, 'countries': countries})
    else:
        form = AddHotelForm
    return render(request, 'main/add_hotel.html', {'form': form, 'countries': countries})


@login_required
def delete_hotel(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    hotel.delete()
    return redirect("hotel_list")


def sort_hotels(request):
    sort_param = request.GET.get('sort')

    hotels = Hotel.objects.all()

    if sort_param == 'name':
        hotels = hotels.order_by('name')
    elif sort_param == 'stars':
        hotels = hotels.order_by('stars')
    # Add more conditions for other sorting options as needed
    # ...

    return render(request, 'main/hotel_list.html', {'hotels': hotels})


def hotel_detail(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    if not request.user.is_staff:
        return render(request, 'main/hotel_detail.html', {'hotel': hotel})
    else:
        countries = Country.objects.all()
        if request.method == 'POST':
            form = AddHotelForm(request.POST, instance=hotel)
            if form.is_valid():
                form.save()
                return redirect('hotel_list')
            else:
                return render(request, 'main/hotel_detail.html', {'form': form, 'countries': countries, 'hotel': hotel})
        else:
            form = AddHotelForm
        return render(request, 'main/hotel_detail.html', {'form': form, 'countries': countries, 'hotel': hotel})


def country_list(request):
    countries = Country.objects.all()
    # Implement any additional filtering or sorting logic based on user input
    return render(request, 'main/country_list.html', {'countries': countries})


def search_countries(request):
    search_query = request.GET.get('q')

    countries = Country.objects.filter(Q(name__icontains=search_query) |
                                       Q(climate_spring__icontains=search_query) |
                                       Q(climate_summer__icontains=search_query) |
                                       Q(climate_autumn__icontains=search_query) |
                                       Q(climate_winter__icontains=search_query))
    # Add more conditions for other sorting options as needed
    # ...

    return render(request, 'main/country_list.html', {'countries': countries})


@login_required
def add_country(request):
    countries = Country.objects.all()
    if request.method == 'POST':
        form = AddCountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
        else:
            return render(request, 'main/add_country.html', {'form': form, 'countries': countries})
    else:
        form = AddCountryForm
    return render(request, 'main/add_country.html', {'form': form, 'countries': countries})


@login_required
def delete_country(request, id):
    country = get_object_or_404(Country, pk=id)
    country.delete()
    return redirect("country_list")


def sort_countries(request):
    sort_param = request.GET.get('sort')

    countries = Country.objects.all()

    if sort_param == 'name':
        countries = countries.order_by('name')
    elif sort_param == 'climate_spring':
        countries = countries.order_by('climate_spring')
    elif sort_param == 'climate_summer':
        countries = countries.order_by('climate_summer')
    elif sort_param == 'climate_autumn':
        countries = countries.order_by('climate_autumn')
    elif sort_param == 'climate_winter':
        countries = countries.order_by('climate_winter')
    # Add more conditions for other sorting options as needed
    # ...

    return render(request, 'main/country_list.html', {'countries': countries})


def country_detail(request, id):
    country = get_object_or_404(Country, pk=id)
    if not request.user.is_staff:
        return render(request, 'main/country_detail.html', {'country': country})
    else:
        if request.method == 'POST':
            form = AddCountryForm(request.POST, instance=country)
            if form.is_valid():
                form.save()
                return redirect('country_list')
            else:
                return render(request, 'main/country_detail.html', {'form': form, 'country': country})
        else:
            form = AddCountryForm
        return render(request, 'main/country_detail.html', {'form': form, 'country': country})


def ticket_list(request):
    # Implement any additional filtering or sorting logic based on user input
    search_query = request.GET.get('search_query', '')
    sort_by = request.GET.get('sort_by', 'name')
    tickets = Ticket.objects.all()

    if search_query:
        tickets = tickets.filter(
            Q(name__icontains=search_query)
        )

    if sort_by == 'name':
        tickets = tickets.order_by('name')
    elif sort_by == 'price':
        tickets = tickets.order_by('price')
    # elif sort_by == 'provider':
    #     products = tickets.order_by('provider__name')

    context = {
        'request': request,
        'tickets': tickets,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, "main/ticket_list.html", context)
    # return render(request, 'main/ticket_list.html', {'tickets': tickets})


@login_required
@permission_required('is_staff')
def client_list(request):
    clients = Client.objects.all()
    # Implement any additional filtering or sorting logic based on user input
    return render(request, 'main/client_list.html', {'clients': clients})


@login_required
@permission_required('is_staff')
def client_detail(request, id):
    client = get_object_or_404(Client, pk=id)
    if not request.user.is_staff:
        return render(request, 'main/country_detail.html', {'client': client})
    else:
        if request.method == 'POST':
            form = AddClientForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                return redirect('client_list')
            else:
                return render(request, 'main/client_detail.html', {'form': form, 'client': client})
        else:
            form = AddCountryForm
        return render(request, 'main/client_detail.html', {'form': form, 'client': client})


@login_required
def order_list(request):
    orders = Order.objects.all()
    sum = 0
    for order in orders:
        # print(order)
        tickets = order.tickets.all()
        # print(tickets)
        for ticket in tickets:
            # print(ticket)
            hotels = ticket.hotels.all()
            # print(hotels)
            sum += ticket.price
            for hotel in hotels:
                print(hotel)
                print(hotel.cost_per_day)
                sum += hotel.cost_per_day
    # Implement any additional filtering or sorting logic based on user input
    print(sum)
    return render(request, 'main/order_list.html', {'orders': orders, 'sum': sum})


@login_required
def order_detail(request, id):
    order = get_object_or_404(Order, pk=id)
    promo = get_object_or_404(PromoCode, pk=order.discount.id)
    client = get_object_or_404(Client, pk=order.client.id)
    tickets = order.tickets.all()
    sum = 0
    for ticket in tickets:
        # print(ticket)
        hotels = ticket.hotels.all()
        # print(hotels)
        sum += ticket.price
    sum = sum * float(100 - promo.discount) / 100
    if request.method == 'POST':
        form = AddOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        else:
            return render(request, 'main/order_detail.html', {'form': form, 'order': order, 'promo': promo, 'tickets': tickets, 'client': client, 'sum': sum})
    else:
        form = AddOrderForm
    return render(request, 'main/order_detail.html', {'form': form, 'order': order, 'promo': promo, 'tickets': tickets, 'client': client, 'sum': sum})

@login_required
def add_order(request):
    tickets = Ticket.objects.all()
    promos = PromoCode.objects.all()
    if request.method == 'POST':
        order_form = AddOrderForm(request.POST)
        client_form = AddClientForm(request.POST)

        if order_form.is_valid() and client_form.is_valid():
            order = order_form.save(commit=False)
            client = client_form.save()
            order.client = client
            order.save()
            selected_tickets = order_form.cleaned_data['tickets']
            order.tickets.set(selected_tickets)
            order.save()
            return redirect(order_list)
        else:
            errors = order_form.errors
            print(errors)
            return render(request, 'main/add_order.html', {'client_form': client_form, 'order_form': order_form, 'tickets': tickets, 'promos': promos})
    else:
        client_form = AddClientForm
        order_form = AddOrderForm
    return render(request, 'main/add_order.html', {'client_form': client_form, 'order_form': order_form, 'tickets': tickets, 'promos': promos})


@login_required
def delete_order(request, id):
    order = get_object_or_404(Order, pk=id)
    order.delete()
    return redirect("order_list")


@login_required
def delete_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    ticket.delete()
    return redirect("ticket_list")


def search_tickets(request):
    search_query = request.GET.get('q')

    tickets = Ticket.objects.filter(Q(name__icontains=search_query) |
                                       Q(duration__icontains=search_query) |
                                       Q(price__icontains=search_query))
    # Add more conditions for other sorting options as needed
    # ...

    return render(request, 'main/ticket_list.html', {'tickets': tickets})


def sort_tickets(request):
    sort_param = request.GET.get('sort')

    tickets = Ticket.objects.all()

    if sort_param == 'name':
        tickets = tickets.order_by('name')
    elif sort_param == 'duration':
        tickets = tickets.order_by('duration')
    elif sort_param == 'price':
        tickets = tickets.order_by('price')
    # Add more conditions for other sorting options as needed
    # ...

    return render(request, 'main/ticket_list.html', {'tickets': tickets})


def ticket_detail(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    hotels = ticket.hotels.all()
    if not request.user.is_staff:
        return render(request, 'main/ticket_detail.html', {'ticket': ticket, 'hotels': hotels})
    else:
        if request.method == 'POST':
            form = AddCountryForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('ticket_list')
            else:
                return render(request, 'main/ticket_detail.html', {'form': form, 'ticket': ticket, 'hotels': hotels})
        else:
            form = AddCountryForm
        return render(request, 'main/ticket_detail.html', {'form': form, 'ticket': ticket, 'hotels': hotels})


@login_required
def add_ticket(request):
    hotels = Hotel.objects.all()
    if request.method == 'POST':
        ticket_form = AddTicketForm(request.POST)
        # if ticket_form.is_valid():
        #     ticket_form.save()
        # else:
        #     print("not valid")
        # # print(ticket_form)
        # ticket_name = ticket_form["name"]
        # ticket_duration = ticket_form["duration"]
        # print(ticket_duration)
        # ticket_place = ticket_form["price"]
        # ticket_hotels = request.POST.getlist("id_hotels")
        # print(ticket_hotels)
        # print("--------")
        # print(ticket_form.fields["hotels"])
        # print("--------")
        # # print(ticket_hotels)
        # ticket_countries = []
        # for hotel_id in ticket_hotels:
        #     # print(hotel_id.data)
        #
        #     print("id")
        #     print(hotel_id.data["value"].value)
        #     # print(hotel_id.data["value"])
        #     hotel = Hotel.objects.get(id=hotel_id.data["value"].value)
        #     ticket_countries.append(hotel.country.id)
        # ticket_tmp = Ticket(name=ticket_name, hotels=ticket_hotels, countries=ticket_countries,
        #                     duration=ticket_duration, price=ticket_place)
        # ticket_tmp.save()
        # ticket_form.fields["countries"] = countries
        # print(ticket_form.fields["countries"])
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('ticket_list')
        else:
            print("error")
            errors = ticket_form.errors
            print(errors)
            return render(request, 'main/add_ticket.html', {'ticket_form': ticket_form, 'hotels': hotels})
    else:
        ticket_form = AddTicketForm
    return render(request, 'main/add_ticket.html', {'ticket_form': ticket_form, 'hotels': hotels})





# Create your views here.

# def index(request):
#     people = Person.objects.all()
#     return render(request, "index.html", {"people": people})
#
#
# # сохранение данных в бд
# def create(request):
#     if request.method == "POST":
#         person = Person()
#         person.name = request.POST.get("name")
#         person.age = request.POST.get("age")
#         person.save()
#     return HttpResponseRedirect("/")
#
#
# # изменение данных в бд
# def edit(request, id):
#     try:
#         person = Person.objects.get(id=id)
#
#         if request.method == "POST":
#             person.name = request.POST.get("name")
#             person.age = request.POST.get("age")
#             person.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"person": person})
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")
#
#
# # удаление данных из бд
# def delete(request, id):
#     try:
#         person = Person.objects.get(id=id)
#         person.delete()
#         return HttpResponseRedirect("/")
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")
