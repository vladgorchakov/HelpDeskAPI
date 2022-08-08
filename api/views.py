from rest_framework import viewsets
from api.serializers import TicketListSerializer, TicketCreateSerializer, SupportTicketDetailSerializer, \
 TicketDetailSerializer, MessageSerializer, MessageDetailSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.permissions import IsAuthor
from helpdesk.models import Ticket, Message


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action == 'list':
            return TicketListSerializer
        elif self.action == 'create':
            return TicketCreateSerializer
        if self.request.user.is_staff:
            if self.request.user != Ticket.objects.get(pk=self.kwargs['pk']).user:
                return SupportTicketDetailSerializer

        return TicketDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        else:
            return Message.objects.filter(ticket__user=self.request.user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return MessageSerializer
        return MessageDetailSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated, ]
        else:
            permission_classes = [IsAuthor, ]

        return [permission() for permission in permission_classes]
