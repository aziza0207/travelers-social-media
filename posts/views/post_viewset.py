from copy import deepcopy

from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from slugify import slugify
from ..models import Post
from ..serialzers import PostSerializer, PostCreateSerializer
from ..services import PostService


@extend_schema(tags=["Post"])
class PostViewSet(viewsets.ModelViewSet):
    lookup_field = "pk"

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.action == self.list.__name__:
            return queryset.select_related("country").order_by("-created_at")[:10]
        return queryset

    def get_serializer_class(self):
        if self.action == self.list.__name__:
            return PostSerializer
        if self.action == self.create.__name__:
            return PostCreateSerializer
        if self.action == self.my_subscribed_posts.__name__:
            return PostSerializer

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
        serializer = self.get_serializer(user_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
