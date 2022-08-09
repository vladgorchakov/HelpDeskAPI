from rest_framework import permissions


class IsMessageAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user


class IsTicketAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff
