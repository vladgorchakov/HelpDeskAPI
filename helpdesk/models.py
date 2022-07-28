from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.pk
