import logging

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from helpdesk import models
from api.tasks import send_email


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = "__all__"
        model = models.Message


class TicketMessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = models.Message
        fields = ('id', 'ticket', 'sender', 'text')


class TicketMessageCreateSerializer(MessageSerializer):
    class Meta:
        model = models.Message
        fields = ('sender', 'text', 'past_message')

class TicketMessageUpdateSerializer(MessageSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)




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
    messages = TicketMessageCreateSerializer(many=True)

    def create(self, validated_data):
        msgs = validated_data.pop('messages')
        ticket = models.Ticket.objects.create(**validated_data)

        for msg in msgs:
            models.Message.objects.create(ticket=ticket, **msg)

        return ticket

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        print(instance.user)

        for msg in validated_data['messages']:
            try:
                msg_instance = models.Message.objects.get(pk=msg['id'])
            except ObjectDoesNotExist:
                logging.error('Message does not exists')
            else:
                msg_instance.text = msg.get('text', msg_instance)
                msg_instance.save()

        return instance

    def validate(self, attrs):
        print('ATTRS:', attrs['user'])
        messages_data = attrs['messages']
        print(messages_data)
        for msg in messages_data:
            if not models.Message.objects.filter(pk=msg['id']).exists():
                raise serializers.ValidationError({'detail': f'Message with id={msg["id"]} does not exists'})
            if msg['sender'] != attrs['user']:
                detail = {'detail': f'{msg["user"]} is not sender of message with id={msg["id"]}'}
                raise serializers.ValidationError(detail=detail)
        return attrs

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
    messages = MessageSerializer(many=True, read_only=True)

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
