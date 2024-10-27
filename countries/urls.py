from django.urls import path
from .views import CountryViewSet, CountrySubscriptionViewSet

urlpatterns = [
    path("", CountryViewSet.as_view({"get": "list"}), name="country-list"),
    path(
        "<str:slug>",
        CountryViewSet.as_view({"get": "retrieve"}),
        name="country-detail",
    ),
    path(
        "subscribe/<str:slug>/",
        CountrySubscriptionViewSet.as_view({"post": "subscribe"}),
        name="subscribe-country",
    ),
    path(
        "unsubscribe/<str:slug>/",
        CountrySubscriptionViewSet.as_view({"delete": "unsubscribe"}),
        name="unsubscribe-country",
    ),
]
