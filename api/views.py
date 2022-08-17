from rest_framework import viewsets
from api.serializers import (
                             TicketListSerializer,
                             TicketCreateSerializer,
                             SupportTicketDetailSerializer,
                             TicketDetailSerializer,
                             MessageSerializer,
                             MessageDetailSerializer)

from rest_framework.permissions import IsAuthenticated
from api.permissions import IsMessageAuthor, IsTicketAuthorOrStaff
from helpdesk.models import Ticket, Message


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTicketAuthorOrStaff]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user).order_by('-update_time')

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return TicketListSerializer
            case 'create':
                return TicketCreateSerializer

        if self.request.user.is_staff and self.request.user != Ticket.objects.get(pk=self.kwargs['pk']).user:
            return SupportTicketDetailSerializer

        return TicketDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsMessageAuthor, ]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        else:
            return Message.objects.filter(sender=self.request.user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return MessageSerializer
        return MessageDetailSerializer
