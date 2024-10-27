from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import UserSubscription, User
from ..serializers import UserSubscriptionCreateSerializer


@extend_schema(tags=["UserSubscription"])
class UserSubscriptionViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSubscriptionCreateSerializer
    queryset = UserSubscription.objects.all()
    lookup_field = "user_pk"

    def get_queryset(self):
        return self.queryset.filter(subscriber=self.request.user)

    @action(detail=False, methods=["post"])
    def subscribe(self, request, user_pk=None):
        subscribed_to = get_object_or_404(User, pk=user_pk)
        subscription, created = UserSubscription.objects.get_or_create(subscriber=request.user,
                                                                       subscribed_to=subscribed_to)

        if created:
            return Response({"detail": "Вы успешно подписались"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Вы успешно уже подписаны"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["delete"])
    def unsubscribe(self, request, user_pk=None):
        subscribed_to = get_object_or_404(User, pk=user_pk)
        subscription = UserSubscription.objects.filter(subscriber=request.user, subscribed_to=subscribed_to).first()

        if subscription:
            subscription.delete()
            return Response({"detail": "Вы успешно отписались"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Вы не подписаны"}, status=status.HTTP_400_BAD_REQUEST)
