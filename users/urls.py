from django.urls import path
from .views import UserViewSet, UserSubscriptionViewSet

urlpatterns = [
    path(
        "register/",
        UserViewSet.as_view({"post": "register"}),
        name="user-register",
    ),
    path("login/", UserViewSet.as_view({"post": "login"}), name="user-login"),
    path("", UserViewSet.as_view({"get": "list"}), name="user-list"),
    path(
        "<int:pk>/", UserViewSet.as_view({"get": "retrieve"}), name="user-detail"
    ),
    path(
        "<int:pk>/", UserViewSet.as_view({"get": "retrieve"}), name="user-detail"
    ),
    path(
        "subscribe/",
        UserSubscriptionViewSet.as_view({"post": "subscribe"}),
        name="user-subscribe",
    ),
    path(
        "unsubscribe/",
        UserSubscriptionViewSet.as_view({"delete": "subscribe"}),
        name="user-unsubscribe",
    ),
]
