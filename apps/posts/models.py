from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation
)
from django.contrib.contenttypes.models import ContentType


class Vote(models.Model):
    """Model of some object's vote. """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="votes",
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"Upvote {self.user} of ({self.content_object})"


class Comment(models.Model):
    """Model of comment"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE
    )
    votes = GenericRelation(Vote)

    def __str__(self):
        return f"Comment {self.author} of" \
               f" {self.parent if self.parent else self.object_id} " \
               f"{self.content_type}"

    class Meta:
        ordering = ("-creation_date",)

    @property
    def votes_num(self):
        return self.votes.count()


class Post(models.Model):
    """Model of post"""

    title = models.CharField(max_length=64, unique=True)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    votes = GenericRelation(Vote)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    comments = GenericRelation(Comment)

    class Meta:
        ordering = ("-creation_date",)

    def __str__(self):
        return f"{self.title} -- {self.author}"

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.id])

    @property
    def votes_num(self):
        return self.votes.count()

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
