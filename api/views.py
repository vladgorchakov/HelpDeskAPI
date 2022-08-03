from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import Group, User
from api import serializers
from helpdesk import models


class UserTicketViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserTicketSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Ticket.objects.filter(user=user)


class SupportTicketViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = serializers.SupportTecketSerializer
    queryset = models.Ticket.objects.all()

    def list(self, request, *args, **kwargs):
        if 'status' in request.data:
            status = request.data['status']
            try:
                queryset = models.Ticket.objects.filter(status=status)
            except ValueError:
                return Response({'error': 'ValueError'})

        else:
            queryset = models.Ticket.objects.all()

        serializer = serializers.SupportTecketSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return models.Ticket.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        user = self.request.user
        msg = models.Message.objects.filter(ticket__user=user)
        return msg

    # def get_queryset(self):
    #     user = self.request.user
    #     # user = User.objects.get(username=self.request.user)
    #     group = Group.objects.get(name='HelpDeskUser')
    #     print(group)
    #     print(user.groups.all())
    #     return models.Message.objects.all()
