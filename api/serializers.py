from rest_framework import serializers
from helpdesk import models


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = "__all__"
        model = models.Message


class MessageDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = "__all__"
        model = models.Message
        read_only_fields = ('ticket',)


class TicketMessageCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Message
        fields = ('user', 'text')


class TicketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    messages = TicketMessageCreateSerializer(many=True, allow_null=True)

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
    messages = MessageDetailSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Ticket
        fields = '__all__'
        read_only_fields = ('status', 'messages')


class SupportTicketDetailSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=models.Ticket.Status.choices)
    messages = MessageDetailSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Ticket
        fields = '__all__'
        read_only_fields = ('user', 'title', 'description')
