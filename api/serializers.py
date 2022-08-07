from django.contrib.auth.models import User
from rest_framework import serializers
from helpdesk import models
from api.tasks import send_email


class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = models.Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Message
        fields = ('id', 'sender', 'text', 'past_message',)


class TicketReadOnlySerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    status = serializers.IntegerField(read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Ticket
        fields = ('id', 'user', 'title', 'status',)


class TicketDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.ChoiceField(choices=models.Ticket.Status.choices,
                                     default=models.Ticket.Status.added,
                                     read_only=True
                                     )
    messages = MessageSerializer(many=True)

    def create(self, validated_data):
        msgs = validated_data.pop('messages')
        ticket = models.Ticket.objects.create(**validated_data)

        for msg in msgs:
            print(msg)
            models.Message.objects.create(ticket=ticket, **msg)

        return ticket

    class Meta:
        model = models.Ticket
        fields = ('id', 'user', 'title', 'status', 'description', 'messages')


class SupportTicketDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    status = serializers.ChoiceField(choices=models.Ticket.Status.choices,
                                     default=models.Ticket.Status.added,
                                     )

    def update(self, instance, validated_data):
        if validated_data['status'] != instance.status:
            instance.status = validated_data['status']
            instance.save()
            send_email.delay(instance.user.email,
                             models.Ticket.Status.choices[validated_data['status']][1]
                             )
        return instance

    class Meta:
        model = models.Ticket
        fields = '__all__'
