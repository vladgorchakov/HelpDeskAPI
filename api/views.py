from rest_framework import viewsets
from api import serializers
from helpdesk import models


class UserTicketViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserTicketSerializer
    queryset = models.Ticket.objects.all()
