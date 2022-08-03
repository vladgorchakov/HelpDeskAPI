from rest_framework import viewsets, mixins
from api import serializers
from helpdesk import models


class UserTicketViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserTicketSerializer
    queryset = models.Ticket.objects.all()


class SupportTicketViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = serializers.SupportTecketSerializer
    queryset = models.Ticket.objects.all()

