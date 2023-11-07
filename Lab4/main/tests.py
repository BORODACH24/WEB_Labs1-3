from django.test import TestCase

# Create your tests here.
import pytest
from django.test import Client, RequestFactory
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from .models import Ticket, Hotel


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    return user


def test_client_connection(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_creation(user):
    assert User.objects.count() == 1
    assert User.objects.first().username == 'testuser'


@pytest.mark.django_db
def test_database_connection():
    with connection.cursor() as cursor:
        cursor.execute('SELECT 1')
        result = cursor.fetchone()

    assert result == (1,)


@pytest.mark.django_db
def test_login_user_form_valid(client, user):
    login_url = '/login/'
    form_data = {'username': 'testuser', 'password': 'testpassword'}
    response = client.post(login_url, data=form_data)
    assert response.status_code == 302  # Expect a redirect
    assert authenticate(username='testuser', password='testpassword') == user
    assert client.session['_auth_user_id'] == str(user.pk)
    assert client.session['_auth_user_backend'] == 'django.contrib.auth.backends.ModelBackend'
    assert client.get(response.url).status_code == 200  # Expect a successful response for the redirected page


@pytest.mark.django_db
def test_login_user_form_invalid(client):
    login_url = '/login/'
    form_data = {'username': 'testuser', 'password': 'wrongpassword'}
    response = client.post(login_url, data=form_data)
    assert response.status_code == 200  # Expect a successful response
    assert 'form' in response.context  # Expect the form to be passed to the context


@pytest.fixture
def ticket():
    ticket = Ticket.objects.create(name='Test Ticket')
    return ticket


@pytest.mark.django_db
def test_provider_list(client, provider):
    url = reverse('providers_list')
    response = client.get(url)

    assert response.status_code == 200
    assert 'providers' in response.context
    assert len(response.context['providers']) == 1
    assert response.context['providers'][0].name == 'Test Provider'

