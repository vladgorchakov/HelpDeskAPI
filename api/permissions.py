from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from helpdesk.models import Ticket


class IsMessageAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user


class IsTicketAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class MessagePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        match view.action:
            case 'list':
                return bool(request.user.is_staff)
            case 'retrieve':
                return bool(request.user == obj.sender or request.user.is_staff)
            case 'update':
                print('update')
                return bool(request.user == obj.sender)
            case 'create':
                print('create', obj.ticket.user, request.user)
                # return bool(request.user == obj.ticket.user)
                return False
            case 'destroy':
                return bool(request.user == obj.sender)
