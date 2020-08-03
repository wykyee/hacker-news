from rest_framework import serializers

from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = serializers.PrimaryKeyRelatedField(many=True,
                                                  read_only=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "author",
            "link",
            "creation_date",
            "votes_num",
            "id",
            "comments",
        )

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        post = Post.objects.create(**validated_data)

        return post

