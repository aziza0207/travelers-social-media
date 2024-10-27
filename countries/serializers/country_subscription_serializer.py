from rest_framework import serializers
from ..models import Country, CountrySubscription


class CountrySubscriptionSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all())

    class Meta:
        model = CountrySubscription
        fields = ("country",)
