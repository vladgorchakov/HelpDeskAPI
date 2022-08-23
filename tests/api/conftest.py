import pytest
from rest_framework.test import APIClient

from .testuser import TestUser


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user():


@pytest.fixture(scope='session')
def get_user():
    user = TestUser(
        username='helpdeskuser',
        password='testPass12345',
        email='helpdeskuser@helpdesk.com'
    )

    return user
