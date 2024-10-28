from rest_framework import serializers
from ..models import Country, CountrySubscription


class CountrySubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CountrySubscription
        fields = ("user",)



