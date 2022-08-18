from django.contrib.auth.models import User
from django.db import models


class TimeMixin(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ticket(TimeMixin):
    class Status(models.IntegerChoices):
        added = 0
        accepted = 1
        frozen = 2
        resolved = 3
        unresolved = 4

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, default=Status.added)

    def __str__(self):
        return f'{self.title} [{self.pk}]'

    def __int__(self):
        return self.pk


class Message(TimeMixin):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.text

    def __int__(self):
        return self.pk
