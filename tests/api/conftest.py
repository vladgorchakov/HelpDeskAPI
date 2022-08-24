import pytest
from rest_framework.test import APIClient
from tests.api.users.testuser import TestUser


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture(scope='session')
def user():
    user = TestUser(
        username='helpdeskuser',
        password='testPass12345',
        email='helpdeskuser@helpdesk.com'
    )
    return user


@pytest.fixture
def created_user(user, client):
    user = TestUser(
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

    return client
