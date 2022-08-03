from rest_framework import serializers
from helpdesk import models


class UserTicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField('title', read_only=True)

    class Meta:
        model = models.Ticket
        fields = ('user', 'title', 'description', 'status', 'create_time', 'update_time')


class SupportTecketSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    status = serializers.SlugRelatedField(slug_field='title', queryset=models.Status.objects.all())


    class Meta:
        model = models.Ticket
        fields = '__all__'
