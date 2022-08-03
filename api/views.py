from rest_framework import viewsets, mixins
from rest_framework.response import Response

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
