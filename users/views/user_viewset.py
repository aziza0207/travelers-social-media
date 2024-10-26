from django.db.models import Prefetch, OuterRef, Subquery, Count
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from posts.models import Post
from users.serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserListSerializer,
    UserDetailSerializer,
)


@extend_schema(tags=["User"])
class UserViewSet(viewsets.ModelViewSet):
    lookup_field = "pk"

    def get_queryset(self):
        queryset = User.objects.all()
        if self.action == self.list.__name__:
            return queryset.annotate_posts_count().annotate_countries_count()
        if self.action == self.retrieve.__name__:
            return queryset.prefetch_related(
                Prefetch(
                    "author_posts", queryset=Post.objects.all().select_related("country").order_by("country__id")
                )
            )
        return queryset

    def get_serializer_class(self):
        if self.action == self.register.__name__:
            return UserRegisterSerializer
        if self.action == self.login.__name__:
            return UserLoginSerializer
        if self.action == self.list.__name__:
            return UserListSerializer
        if self.action == self.retrieve.__name__:
            return UserDetailSerializer

    @action(detail=False, methods=["POST"])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        existing_user = self.get_queryset().filter(email=email).first()

        if existing_user:
            raise ValidationError("Пользователь с таким email уже существует!")

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        tokens = {"access_token": str(refresh.access_token), "refresh": str(refresh)}

        return Response({"tokens": tokens}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("User not found")
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            data = {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }

            serializer.validated_data["tokens"] = data
            return Response(data, status=status.HTTP_200_OK)
        else:
            raise AuthenticationFailed("Invalid credentials")
