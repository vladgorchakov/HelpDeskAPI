from rest_framework import serializers
from helpdesk.models import Ticket, Status, Message


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    ticket = serializers.SlugRelatedField(slug_field='title', queryset=Ticket.objects.all())
    past_message = serializers.SlugRelatedField(slug_field='text', queryset=Message.objects.all())

    class Meta:
        model = Message
        fields = '__all__'
