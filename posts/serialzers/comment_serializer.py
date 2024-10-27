from rest_framework import serializers
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализатор комментария к посту"""

    class Meta:
        model = Comment
        exclude = ("post",)


class CommentCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания комментария к посту"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ("post", "user", "content")
