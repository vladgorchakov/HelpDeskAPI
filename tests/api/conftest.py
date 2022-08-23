import pytest


@pytest.fixture(scope='session')
def get_user_payload():
    payload = {
        "email": "user@helpdesk.com",
        "username": "helpdeskuser",
        "password": "helpdeskPassword54"
    }

    return payload
