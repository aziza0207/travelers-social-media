from rest_framework import serializers
from ..models import PostRating, Post


class PostRatingSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostRating
        fields = ("user", "post", "rating")
