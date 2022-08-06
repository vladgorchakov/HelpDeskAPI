from rest_framework import viewsets, mixins
from rest_framework.response import Response
from api import serializers
from helpdesk import models
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.permissions import IsAuthor


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TicketReadOnlySerializer

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return models.Ticket.objects.all()
        return models.Ticket.objects.filter(user=user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TicketReadOnlySerializer
        elif self.action == 'update' and self.request.user.is_staff:
            if self.request.user != models.Ticket.objects.get(pk=self.kwargs['pk']).user:
                return serializers.SupportTicketDetailSerializer

        return serializers.TicketDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthor,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Message.objects.all()
        else:
            return models.Message.objects.filter(ticket__user=self.request.user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MessageListSerializer
        return serializers.MessageSerializer
