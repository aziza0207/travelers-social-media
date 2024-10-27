from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TagSubscription, Tag
from common.permissions import IsAuthenticatedNotAdmin


@extend_schema(tags=["TagSubscription"])
class TagSubscriptionViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticatedNotAdmin,)
    queryset = TagSubscription.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=["post"])
    def subscribe(self, request, tag_pk=None):
        tag = get_object_or_404(Tag, pk=tag_pk)
        subscription, created = TagSubscription.objects.get_or_create(user=request.user, tag=tag)

        if created:
            return Response({"detail": "Вы успешно подписались"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Вы уже подписаны"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def unsubscribe(self, request, tag_pk=None):
        tag = get_object_or_404(Tag, pk=tag_pk)
        subscription = TagSubscription.objects.filter(user=request.user, tag=tag).first()

        if subscription:
            subscription.delete()
            return Response({"detail": "Вы успешно отподписались"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Не были подписаны"}, status=status.HTTP_400_BAD_REQUEST)
