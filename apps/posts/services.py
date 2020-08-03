from django.contrib.contenttypes.models import ContentType

from .models import Post, Vote


def get_all_posts():
    return Post.objects.all()


def get_votes_to_posts():
    """
    Returns queryset of votes, that are connected to posts.
    """
    obj_type = ContentType.objects.get_for_model(Post)
    return Vote.objects.filter(content_type=obj_type)


def upvote(obj, user):
    """
    Add vote to object(Comment, Post etc.).
    """
    obj_type = ContentType.objects.get_for_model(obj)
    vote, is_created = Vote.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user
    )
    return vote


def unvote(obj, user):
    """
    Delete vote of object.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Vote.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()
