from django.contrib.auth import get_user_model
from .models import Post, Comment
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = [
            "author",
            "post",
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("post")
        return ret


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
