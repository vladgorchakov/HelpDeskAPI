from django.contrib import admin
from helpdesk.models import Ticket, Message


admin.site.register(Ticket)
admin.site.register(Message)
