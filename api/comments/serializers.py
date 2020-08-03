from rest_framework import serializers

from apps.posts.models import Comment, Post
from django.contrib.contenttypes.models import ContentType


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = (
            "author",
            "content",
            "creation_date",
            "votes_num",
            "id",
            "parent",
            "replies",
        )

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user

        content_type = ContentType.objects.get_for_model(Post)
        obj_id = self.context.get("post_id")
        parent_id = self.context.get("parent_id", None)

        comment = Comment.objects.create(
            author=validated_data["author"],
            content=validated_data["content"],
            parent_id=parent_id,
            object_id=obj_id,
            content_type=content_type
        )

        return comment
