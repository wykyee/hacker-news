from rest_framework.decorators import action
from rest_framework.response import Response

from apps.posts import services


class VoteMixin:
    """
    Mixin that provides possibility to vote. Must be inherited
    after GenericApiView
    """
    @action(methods=["POST"], detail=True)
    def upvote(self, request, pk=None):
        """
        Adds vote to certain object(Post, Comment)
        """
        obj = self.get_object()
        services.upvote(obj, request.user)
        return Response({
            "Voted": True,
            "Post ID": pk,
            "User": request.user.username
        })

    @action(methods=["POST"], detail=True)
    def unvote(self, request, pk=None):
        """
        Removes vote to certain object
        """
        obj = self.get_object()
        services.unvote(obj, request.user)
        return Response({
            "Unvoted": True,
            "Post ID": pk,
            "User": request.user.username
        })

    def get_object(self):
        pass
