from django.urls import path
from .views import TagSubscriptionViewSet


urlpatterns = [
    path(
        "subscribe/<str:slug>/",
        TagSubscriptionViewSet.as_view({"post": "subscribe"}),
        name="subscribe-tag",
    ),
    path(
        "unsubscribe/<str:slug>/",
        TagSubscriptionViewSet.as_view({"delete": "unsubscribe"}),
        name="unsubscribe-tag",
    ),
]

