from rest_framework import serializers
from ..models import Country
from posts.serialzers import PostSerializer


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class CountryDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(source="country_posts", many=True)

    class Meta:
        model = Country
        fields = "__all__"
