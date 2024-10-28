from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import CountrySubscription, Country
from ..serializers import CountrySubscriptionSerializer


@extend_schema(tags=["CountrySubscription"])
class CountrySubscriptionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = CountrySubscriptionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CountrySubscription.objects.all()
    lookup_field = "slug"

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    @action(detail=False, methods=["post"])
    def subscribe(self, request, slug=None):
        country = get_object_or_404(Country, slug=slug)
        subscription, created = CountrySubscription.objects.get_or_create(user=request.user, country=country)

        if created:
            return Response({"detail": "Вы успешно подписались"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Вы уже подписаны"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["delete"])
    def unsubscribe(self, request, slug=None):
        country = get_object_or_404(Country, slug=slug)
        subscription = CountrySubscription.objects.filter(user=request.user, country=country).first()

        if subscription:
            subscription.delete()
            return Response({"detail": "Вы успешно отподписались"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Не были подписаны"}, status=status.HTTP_400_BAD_REQUEST)
