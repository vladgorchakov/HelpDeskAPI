from django.contrib import admin
from helpdesk.models import Status, Ticket, Message


admin.site.register(Status)
admin.site.register(Ticket)
admin.site.register(Message)
