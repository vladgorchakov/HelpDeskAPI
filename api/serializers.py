from django.contrib.auth.models import User
from rest_framework import serializers
from helpdesk import models
from api.tasks import send_email


class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'sender', 'past_message', 'text')
        model = models.Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    ticket = serializers.SlugRelatedField(slug_field='id',
                                          queryset=models.Ticket.objects.all()
                                          )
    past_message = serializers.SlugRelatedField(slug_field='id', queryset=models.Message.objects.all(), allow_null=True, allow_empty=True)

    # def validate(self, value):
    #     super().validate(value)
    #     user_id = self.context['request'].user.id
    #     ticket_id = self.context['request'].data['ticket']
    #
    #     past_message_id = self.context['request'].data['past_message']
    #     print(past_message_id)
    #
    #     ticket = models.Ticket.objects.get(pk=ticket_id)
    #     past_message = models.Message.objects.get(pk=past_message_id)
    #     if not User.objects.get(pk=user_id).is_superuser:
    #         if not ticket.user.pk == user_id:
    #             raise serializers.ValidationError(
    #                 'User is not owner of this ticket'
    #             )
    #         elif not past_message.sender.pk == user_id:
    #             raise serializers.ValidationError(
    #                 'User is not owner of past message'
    #             )
    #
    #     return value

    class Meta:
        model = models.Message
        fields = ('id', 'sender', 'ticket', 'text', 'past_message',)


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

    class Meta:
        model = models.Ticket
        fields = '__all__'


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
