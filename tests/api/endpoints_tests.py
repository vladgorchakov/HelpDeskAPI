import pytest
from rest_framework.test import APIClient


class TestUser:
    def __init__(self, user_payload):
        self.username = user_payload['username']
        self.email = user_payload['email']
        self.__password = user_payload['password']


client = APIClient()
url = 'http://0.0.0.0:8000/'


@pytest.mark.django_db
def test_register_user(get_user_payload):
    endpoint = "api/v1/auth/users/"
    user = TestUser(get_user_payload)
    response = client.post(url + endpoint, get_user_payload)

    assert response.status_code == 201

    assert response.data['username'] == user.username
    assert response.data['email'] == user.email
    assert 'password' not in response.data

    # Дописать валидацию с базой данных


@pytest.mark.django_db
def test_login_user(get_user_payload):
    endpoint = 'api/v1/drf-auth/login/'
    response = client.post(url + endpoint, get_user_payload)

    assert response.status_code == 200
