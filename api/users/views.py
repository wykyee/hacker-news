from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import UserSerializer, UserCreateSerializer
from .permissions import UserProfileReadUpdatePermission
from apps.users import services


class UserViewSet(viewsets.ModelViewSet):
    queryset = services.get_all_users()

    def get_permissions(self):
        """
        GET(list), DELETE: user is admin
        POST: anyone
        PUT, PATCH, GET(retrieve): user is admin or it is user's profile
        """
        if self.action == "create":
            permission_classes = [AllowAny]
        elif self.action in ["retrieve", "update", "partial_update"]:
            permission_classes = [UserProfileReadUpdatePermission]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action != "create":
            return UserSerializer
        else:
            return UserCreateSerializer
