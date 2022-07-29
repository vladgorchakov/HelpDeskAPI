from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.pk


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} [{self.pk}]'

    def __int__(self):
        return f'{self.pk}'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    past_message = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text

    def __int__(self):
        return self.pk
