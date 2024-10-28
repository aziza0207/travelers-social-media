from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from ..serialzers import PostRatingSerializer
from ..models import PostRating
from common.permissions import IsAuthenticatedNotAdmin


@extend_schema(tags=["PostRating"])
class PostRatingViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = (IsAuthenticatedNotAdmin,)
    serializer_class = PostRatingSerializer
    queryset = PostRating.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        post = serializer.validated_data["post"]
        if post_rate := self.get_queryset().filter(post=post, user=user).first():
            post_rate.rating = serializer.validated_data["rating"]
            post_rate.save()
        else:
            post_rate = PostRating(
                user=self.request.user,
                post=post,
                rating=serializer.validated_data["rating"],
            )
            post_rate.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
