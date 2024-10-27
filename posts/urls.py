from django.urls import path
from .views import PostViewSet

urlpatterns = [
    path("posts/", PostViewSet.as_view({"get": "list"}), name="post-list"),
    path("posts/create/", PostViewSet.as_view({"post": "create"}), name="post-create"),
    path(
        "posts/subscribed/",
        PostViewSet.as_view({"get": "my_subscribed_posts"}),
        name="subscribed-posts",
    ),
]
