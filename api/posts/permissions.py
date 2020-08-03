from rest_framework import permissions


class IsAdminOrIsAuthor(permissions.BasePermission):
    """
    Object-level permission to only allow author or staff to update
    or delete item (comment, post, etc.).
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.is_staff
