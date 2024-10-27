from rest_framework import serializers
from ..models import UserSubscription


class UserSubscriptionCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для подписки на пользователя"""

    subscriber = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserSubscription
        fields = ("subscriber",)
