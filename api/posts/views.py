from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import PostSerializer
from .permissions import IsAdminOrIsAuthor
from .mixins import VoteMixin
from apps.posts import services


class PostViewSet(viewsets.ModelViewSet, VoteMixin):
    """
    Viewset that is responsible for work with posts.
    """
    serializer_class = PostSerializer
    queryset = services.get_all_posts()

    def get_permissions(self):
        """
        GET: anyone
        PUT, PATCH, DELETE: user is staff or author
        POST: user is authenticated
        """
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAdminOrIsAuthor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
