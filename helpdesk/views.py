from rest_framework.viewsets import ModelViewSet
from helpdesk.models import Ticket
from helpdesk.serializers import TicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
