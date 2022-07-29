from rest_framework.viewsets import ModelViewSet
from helpdesk.models import Ticket, Message
from helpdesk.serializers import TicketSerializer, MessageSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
