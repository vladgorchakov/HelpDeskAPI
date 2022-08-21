from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

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
        if view.action == 'list':
            return bool(request.user.is_authenticated)
        if view.action == 'create':
            ticket_id = request.data.get('ticket')
            if ticket_id:
                try:
                    return bool(request.user == Ticket.objects.get(pk=ticket_id).user or request.user.is_staff)
                except ObjectDoesNotExist:
                    return True

        return True

    def has_object_permission(self, request, view, obj):
        match view.action:
            case 'retrieve':
                return bool(request.user.is_staff or request.user == obj.sender)
            case 'update':
                print('update')
                return bool(request.user == obj.sender)
            case 'destroy':
                return bool(request.user == obj.sender)
