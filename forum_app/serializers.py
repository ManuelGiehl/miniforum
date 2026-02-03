from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "created_at"]
        extra_kwargs = {"author": {"read_only": True}, "created_at": {"read_only": True}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "text", "author", "created_at"]
        extra_kwargs = {"author": {"read_only": True}, "created_at": {"read_only": True}}
