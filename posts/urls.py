from django.urls import path
from .views import PostViewSet, CommentViewSet

urlpatterns = [
    path("", PostViewSet.as_view({"get": "list"}), name="post-list"),
    path("<int:pk>/", PostViewSet.as_view({"get": "retrieve"}), name="post-detail"),
    path("create/", PostViewSet.as_view({"post": "create"}), name="post-create"),
    path(
        "subscribed/",
        PostViewSet.as_view({"get": "my_subscribed_posts"}),
        name="subscribed-posts",
    ),
    path("comment/",  CommentViewSet.as_view({"post": "create"}), name="comment-create")
]
