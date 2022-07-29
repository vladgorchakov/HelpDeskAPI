from rest_framework import serializers
from helpdesk.models import Ticket, Status, Message


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
