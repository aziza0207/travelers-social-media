from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path("user/register/", UserViewSet.as_view({"post": "register"}), name="user-register"),
    path("user/login/", UserViewSet.as_view({"post": "login"}), name="user-login"),
    path("users/", UserViewSet.as_view({"get": "list"}), name="user-list"),
    path("users/<int:pk>/", UserViewSet.as_view({"get": "retrieve"}), name="user-detail")

]
