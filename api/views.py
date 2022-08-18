from rest_framework import viewsets
from rest_framework.response import Response

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
from api.tasks import send_email
from django.core.exceptions import ObjectDoesNotExist


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTicketAuthorOrStaff]

    def update(self, request, *args, **kwargs):
        try:
            instance = Ticket.objects.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            return Response({'error': 'ticket does not exist'})

        if self.request.user.is_staff and self.request.user != instance.user:
            serializer = SupportTicketDetailSerializer(data=request.data, instance=instance)
        else:
            serializer = TicketDetailSerializer(data=request.data, instance=instance)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_email.delay(instance.user.email,
                         instance.title,
                         Ticket.Status.choices[instance.status]
                         )

        return Response(serializer.data)

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
