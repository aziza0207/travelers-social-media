from copy import deepcopy

from django.db.models import Prefetch
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from slugify import slugify
from ..models import Post, Comment
from ..serialzers import PostSerializer, PostCreateSerializer, PostDetailSerializer
from ..services import PostService
from common.permissions import IsAuthenticatedNotAdmin


@extend_schema(tags=["Post"])
class PostViewSet(viewsets.ModelViewSet):
    """Посты"""

    lookup_field = "pk"

    custom_permission_classes = {
        "create": [IsAuthenticatedNotAdmin],
        "retrieve": [IsAuthenticatedNotAdmin],
        "list": [AllowAny],
        "my_subscribed_posts": [IsAuthenticatedNotAdmin],
    }

    def get_queryset(self):
        queryset = Post.objects.filter(is_visible=True).select_related("country")
        if self.action == self.list.__name__:
            return queryset.order_by("-created_at")[:10]
        if self.action == self.retrieve.__name__:
            return queryset.prefetch_related(
                Prefetch(
                    "comments", queryset=Comment.objects.all().select_related("user").order_by("created_at")
                )
            )
        return queryset

    def get_serializer_class(self):
        if self.action == self.list.__name__:
            return PostSerializer
        if self.action == self.create.__name__:
            return PostCreateSerializer
        if self.action == self.my_subscribed_posts.__name__:
            return PostSerializer
        if self.action == self.retrieve.__name__:
            return PostDetailSerializer

    def get_permissions(self):
        if self.action in self.custom_permission_classes.keys():
            return [
                permission()
                for permission in self.custom_permission_classes[self.action]
            ]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        request_data = deepcopy(request.data)
        images = request_data.pop("images", [])
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["images"] = images
        serializer.validated_data["slug"] = slugify(request.data["name"])
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def my_subscribed_posts(self, request):
        user = self.request.user
        user_posts = PostService.get_subscribed_posts(user).order_by("-created_at")
        page = self.paginate_queryset(user_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(user_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
