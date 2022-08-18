from rest_framework import permissions
from helpdesk.models import Ticket


class IsMessageAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user


class IsTicketAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


# TicketMessageAuthorOrStaff пермиссии для того, кто добавляет сообщения к таске
class IsTicketMessageAuthorOrStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.ticket.user or request.user.is_staff
