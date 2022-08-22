from rest_framework import permissions
from helpdesk.models import Ticket
from django.core.exceptions import ObjectDoesNotExist


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsTicketAuthorOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            ticket_id = request.data.get('ticket', None)
            if ticket_id:
                try:
                    return bool(request.user == Ticket.objects.get(pk=ticket_id).user
                                or request.user.is_staff)
                except ObjectDoesNotExist:
                    return True

        return True
