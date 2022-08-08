from rest_framework import serializers
from helpdesk import models
from api.tasks import send_email


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = "__all__"
        model = models.Message


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Message
        read_only_fields = ('sender', 'ticket', 'past_message')


class TicketMessageCreateSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Message
        fields = ('sender', 'text')


class TicketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    messages = TicketMessageCreateSerializer(many=True)

    class Meta:
        model = models.Ticket
        fields = ('user', 'title', 'description', 'messages')

    def create(self, validated_data):
        msgs = validated_data.pop('messages')
        ticket = models.Ticket.objects.create(**validated_data)

        for msg in msgs:
            models.Message.objects.create(ticket=ticket, **msg)

        return ticket


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = '__all__'


class TicketDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Ticket
        fields = '__all__'
        read_only_fields = ('status', 'messages', 'user')


class SupportTicketDetailSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=models.Ticket.Status.choices)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Ticket
        fields = '__all__'
        read_only_fields = ('user', 'title', 'description')

    def update(self, instance, validated_data):
        if validated_data['status'] != instance.status:
            instance.status = validated_data['status']
            instance.save()
            send_email.delay(instance.user.email,
                             instance.title,
                             models.Ticket.Status.choices[validated_data['status']][1]
                             )
        return instance
