import pytest
from rest_framework.authtoken.admin import User

from helpdesk.models import Ticket


@pytest.mark.django_db
def test_create_one_ticket(auth_client_throw_token):
    endpoint = 'http://0.0.0.0:8000/api/v1/tickets/'
    payload = {
        "title": "My ticket",
        "description": "My description",
        'messages': []
    }

    client, user = auth_client_throw_token
    response = client.post(endpoint, payload, format='json')
    ticket = Ticket.objects.all()

    assert response.status_code == 201
    assert len(ticket) == 1

