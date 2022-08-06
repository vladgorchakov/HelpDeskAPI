from rest_framework import viewsets, mixins
from rest_framework.response import Response
from api import serializers
from helpdesk import models
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.tasks import send_email

class UserTicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return models.Ticket.objects.filter(user=user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserTicketListSerializer
        else:
            return serializers.UserTicketDetailSerializer


class SupportTicketViewSet(mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):

    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        if self.action == 'list':
            status = self.request.data.get('status', None)
            if status:
                try:
                    return models.Ticket.objects.filter(status=status.pk)
                except ValueError:
                    return Response({'tickets': ['status does not exists']})

        return models.Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserTicketListSerializer
        else:
            return serializers.SupportTicketDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return models.Message.objects.filter(ticket__user=user).order_by('-update_time')
