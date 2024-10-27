from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import CountrySubscription, Country


@extend_schema(tags=["CountrySubscription"])
class CountrySubscriptionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = CountrySubscription.objects.all()
    lookup_field = "country_pk"

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    @action(detail=False, methods=["post"])
    def subscribe(self, request, country_pk=None):
        country = get_object_or_404(Country, pk=country_pk)
        subscription, created = CountrySubscription.objects.get_or_create(user=request.user, country=country)

        if created:
            return Response({"detail": "Вы успешно подписались"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Вы уже подписаны"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["delete"])
    def unsubscribe(self, request, country_pk=None):
        country = get_object_or_404(Country, pk=country_pk)
        subscription = CountrySubscription.objects.filter(user=request.user, country=country).first()

        if subscription:
            subscription.delete()
            return Response({"detail": "Вы успешно отподписались"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Не были подписаны"}, status=status.HTTP_400_BAD_REQUEST)
