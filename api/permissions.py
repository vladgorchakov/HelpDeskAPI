from rest_framework import permissions
from helpdesk.models import Ticket
from django.core.exceptions import ObjectDoesNotExist


class IsMessageAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user


class IsTicketAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class MessagePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        match view.action:
            case 'list':
                return bool(request.user.is_authenticated)
            case 'create':
                ticket_id = request.data.get('ticket')
                if ticket_id:
                    try:
                        return bool(request.user == Ticket.objects.get(pk=ticket_id).user or request.user.is_staff)
                    except ObjectDoesNotExist:
                        return True
            case _:
                return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return bool(request.user.is_staff or request.user == obj.sender)
        else:
            return bool(request.user == obj.sender)
