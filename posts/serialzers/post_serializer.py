from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source="country.name")

    class Meta:
        model = Post
        fields = ("name", "country", "description", "created_at")
