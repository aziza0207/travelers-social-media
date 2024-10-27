from django.urls import path
from .views import CountryViewSet, CountrySubscriptionViewSet

urlpatterns = [
    path("countries/", CountryViewSet.as_view({"get": "list"}), name="country-list"),
    path("countries/<int:pk>", CountryViewSet.as_view({"get": "retrieve"}), name="country-detail"),
    path("subscribe-country/<int:country_pk>/", CountrySubscriptionViewSet.as_view({"post": "subscribe"}), name="country-list"),
    path("unsubscribe-country/<int:country_pk>/", CountrySubscriptionViewSet.as_view({"delete": "unsubscribe"}), name="country-detail")
]