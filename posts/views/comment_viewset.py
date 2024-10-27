from rest_framework import viewsets, mixins
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from ..serialzers import CommentCreateSerializer
from ..models import Comment


@extend_schema(tags=["Comment"])
class CommentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
