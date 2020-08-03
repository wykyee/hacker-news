from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from api.posts.mixins import VoteMixin
from apps.posts.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet, VoteMixin):
    """
    Viewset that is responsible for work with comments.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        """
        GET: anyone
        POST: user is authenticated
        other: user is admin
        """
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        elif self.action in ["create", "upvote", "unvote"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        """
        To POST, PUT, DELETE we need to get some data from query.
        Either post_id to create comment without parents or
        parent_id to create nested comment
        """
        context = super(CommentViewSet, self).get_serializer_context()
        if self.action in ["create", "update", "partial_update", "destroy"]:
            context.update({
                "parent_id": self.request.GET.get("parent_id", None),
                "post_id": self.request.GET.get("post_id", None),
            })

        return context
