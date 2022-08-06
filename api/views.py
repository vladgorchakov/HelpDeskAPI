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
        elif self.action == 'create':
            return serializers.TicketDetailSerializer
        if self.request.user.is_staff:
            if self.action == 'create':
                return serializers.TicketDetailSerializer
            elif self.action == 'update':
                if self.request.user == models.Ticket.objects.get(pk=self.kwargs['pk']).user:
                    return serializers.TicketDetailSerializer
                else:
                    return serializers.SupportTicketDetailSerializer
        else:
            if self.action in ('create', 'update'):
                return serializers.TicketDetailSerializer

        return serializers.TicketDetailSerializer



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
            return serializers.TicketReadOnlySerializer
        else:
            return serializers.SupportTicketDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return models.Message.objects.all()
        else:
            return models.Message.objects.filter(ticket__user=user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MessageListSerializer
        return serializers.MessageSerializer
