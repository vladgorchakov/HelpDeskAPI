from rest_framework import serializers
from helpdesk import models


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    ticket = serializers.SlugRelatedField(slug_field='id',
                                          queryset=models.Ticket.objects.all()
                                          )
    past_message = serializers.SlugRelatedField(slug_field='id',
                                                queryset=models.Message.objects.all()
                                                )

    def validate(self, value):
        user_id = self.context['request'].user.id
        ticket_id = self.context['request'].data['ticket']
        past_message_id = self.context['request'].data['past_message']

        ticket = models.Ticket.objects.get(pk=ticket_id)
        if not ticket.user.pk == user_id:
            raise serializers.ValidationError(
                'User is not owner of this ticket'
            )
        return value

    class Meta:
        model = models.Message
        fields = ('id', 'sender', 'ticket', 'text', 'past_message',)


class UserTicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField('title', read_only=True)
    # messages = MessageSerializer(many=True)
    class Meta:
        model = models.Ticket
        fields = ('id', 'user', 'title', 'description', 'status', 'create_time', 'update_time',)


class SupportTecketSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    status = serializers.SlugRelatedField(slug_field='title', queryset=models.Status.objects.all())


    class Meta:
        model = models.Ticket
        fields = '__all__'
