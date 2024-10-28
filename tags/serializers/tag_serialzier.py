from rest_framework import serializers
from ..models import Tag


class TagSubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор для подписки к тегу"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tag
        fields = ("user",)


class TagSerializer(serializers.ModelSerializer):
    """ Сериализатор к тегу"""

    class Meta:
        model = Tag
        fields = ("name",)
