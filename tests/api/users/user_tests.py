import pytest
from django.contrib.auth.models import User

url = 'http://0.0.0.0:8000/'


@pytest.mark.django_db
def test_register_user(client, user):
    endpoint = 'api/v1/auth/users/'
    response = client.post(url + endpoint, user.payload)

    assert response.status_code == 201

    assert response.data['username'] == user.username
    assert response.data['email'] == user.email
    assert 'password' not in response.data

    assert User.objects.get(username=user.username)


@pytest.mark.django_db
def test_login_user(client, created_user):
    endpoint = 'api/v1/token/'
    response = client.post(url + endpoint, created_user.payload)

    assert response.status_code == 200
    assert 'refresh' in response.data
    assert 'access' in response.data


@pytest.mark.django_db
def test_login_user_fail(client, user):
    endpoint = 'api/v1/token/'
    response = client.post(url + endpoint, {'username': 'fdf', 'password': '45'})

    assert response.status_code == 401
    assert 'refresh' not in response.data
    assert 'access' not in response.data


@pytest.mark.django_db
def test_user_info(auth_client_throw_token):
    client = auth_client_throw_token
    endpoint = 'api/v1/auth/users/'
    response = client.get(url + endpoint)

    assert response.status_code == 200


@pytest.mark.django_db
def test_token(auth_client_throw_token):
    endpoints = 'api/v1/'
    client = auth_client_throw_token
    response = client.get(url + endpoints)

    assert response.status_code == 200
