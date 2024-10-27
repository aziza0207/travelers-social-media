from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from countries.models import Country
from ..models import Post, PostImage
from tags.models import Tag
from ..utils import compression_photo
from .comment_serializer import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    """Сериализатор поста."""

    country = serializers.CharField(source="country.name")

    class Meta:
        model = Post
        fields = ("name", "country", "description", "created_at")


class PostCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания поста."""

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(), slug_field="slug", required=False, many=True
    )
    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(), slug_field="slug", required=True
    )

    class Meta:
        model = Post
        fields = ("author", "name", "description", "country", "tags")

    def validate_description(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError(
                "Описание должно быть больше трех символов"
            )
        return value

    def validate(self, attrs):
        if not self.context['request'].user.is_allowed_post:
            raise PermissionDenied("Вам запрещено создавать посты.")
        return super().validate(attrs)

    def create(self, validated_data):
        images = validated_data.pop("images", [])
        if len(images) > 10:
            raise serializers.ValidationError("Вы можете загрузить до 10 фотографий")
        post = super().create(validated_data)
        if images:
            PostImage.objects.bulk_create(compression_photo(post=post, images=images))
        return post


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = PostSerializer.Meta.fields + ("comments",)
