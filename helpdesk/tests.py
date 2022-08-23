import pytest
from django.contrib.auth.models import User
from .models import Ticket


@pytest.mark.django_db
def test_user_ticket_create():
    title = 'Title'
    description = 'Description'
    status = 1
    user = User.objects.create_user('TestUser', 'testuser@user.com', 'simple123')
    ticket = Ticket.objects.create(title=title, description=description, status=status, user=user)

    assert ticket.title == title
    assert ticket.description == description
    assert ticket.status == status
    assert ticket.user.id == user.id
    assert ticket.user.username == user.username
    assert ticket.user.email == user.email

