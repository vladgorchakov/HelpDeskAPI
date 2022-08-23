import pytest
from rest_framework.test import APIClient

url = 'http://0.0.0.0:8000/'


@pytest.mark.django_db
def test_register_user(client, get_user):
    endpoint = 'api/v1/auth/users/'
    user = get_user
    response = client.post(url + endpoint, user.payload)

    assert response.status_code == 201

    assert response.data['username'] == user.username
    assert response.data['email'] == user.email
    assert 'password' not in response.data

    # Дописать валидацию с базой данных


@pytest.mark.django_db
def test_login_user(client, get_user):
    endpoint = 'api/v1/token/'
    response = client.post(url + endpoint, get_user.payload)
    print(response)

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(client, get_user):
    endpoint = 'api/v1/token/'
    response = client.post(url + endpoint, {'username': 'fdf', 'password': '45'})
    print("INCORRECT DATA: ", get_user.payload_incorrect)

    assert response.status_code == 401
