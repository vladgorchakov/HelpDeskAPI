from rest_framework import serializers
from helpdesk import models


class UserTicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Ticket
        fields = ('user', 'title', 'description', 'create_time', 'update_time')
