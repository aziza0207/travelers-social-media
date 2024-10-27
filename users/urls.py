from django.urls import path
from .views import UserViewSet, UserSubscriptionViewSet

urlpatterns = [
    path(
        "user/register/",
        UserViewSet.as_view({"post": "register"}),
        name="user-register",
    ),
    path("user/login/", UserViewSet.as_view({"post": "login"}), name="user-login"),
    path("users/", UserViewSet.as_view({"get": "list"}), name="user-list"),
    path(
        "users/<int:pk>/", UserViewSet.as_view({"get": "retrieve"}), name="user-detail"
    ),
    path(
        "users/<int:pk>/", UserViewSet.as_view({"get": "retrieve"}), name="user-detail"
    ),
    path(
        "user-subscribe/",
        UserSubscriptionViewSet.as_view({"post": "subscribe"}),
        name="user-subscribe",
    ),
    path(
        "user-unsubscribe/",
        UserSubscriptionViewSet.as_view({"delete": "subscribe"}),
        name="user-unsubscribe",
    ),
]
