from rest_framework import permissions


class UserProfileReadUpdatePermission(permissions.BasePermission):
    """
    Object-level permission to only allow user or staff to read info
    about their account and edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.username == obj.username or request.user.is_staff:
            return True
