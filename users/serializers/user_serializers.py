from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.serialzers import PostSerializer

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserListSerializer(serializers.ModelSerializer):
    posts_count = serializers.IntegerField()
    countries_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "posts_count", "countries_count")


class UserDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, source="author_posts")


    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "posts")



