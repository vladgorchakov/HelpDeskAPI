import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tests.api.users.userdata import UserData


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture(scope='session')
def user():
    user = UserData(
        username='helpdeskuser',
        password='testPass12345',
        email='helpdeskuser@helpdesk.com'
    )
    return user


@pytest.fixture
def created_user(user, client):
    user = UserData(
        username='auth_helpdesk_user',
        password='12345PaSuser',
        email='auth_help_desk_user@gmail.com'
    )
    client.post('http://0.0.0.0:8000/api/v1/auth/users/', user.payload)

    return user


@pytest.fixture
def auth_client(created_user, client):
    client.post('http://0.0.0.0:8000/api/v1/drf-auth/login/', created_user.payload)

    return client


@pytest.fixture
def auth_client_throw_token(created_user, client):
    response = client.post('http://0.0.0.0:8000/api/v1/token/', created_user.payload)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    return client, user


@pytest.fixture
@pytest.mark.django_db
def create_admin_user(client):
    user = User.objects.create_superuser(username='admin', password='3344978aSd', email='admin@helpdesk.com')
    return user

@pytest.fixture
def auth_admin_client_throw_token(create_admin_user, client):
    payload = {'username': create_admin_user.username, 'password': create_admin_user.password}
    response = client.post('http://0.0.0.0:8000/api/v1/token/', payload)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    return client, create_admin_user
