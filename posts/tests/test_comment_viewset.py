from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Comment
from .factories import UserFactory
from posts.tests.factories import PostFactory


@mark.django_db
class CommentViewSetTest(APITestCase):
    def setUp(self):
        self.create_url: str = reverse("comment-create")

    def test_create_post(self):
        user = UserFactory()
        post = PostFactory()

        payload = {
            "post": post.id,
            "content": "TestComment",


        }
        self.client.force_login(user)
        self.assertEqual(Comment.objects.count(), 0)
        with self.assertNumQueries(7):
            res = self.client.post(self.create_url, data=payload)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Comment.objects.count(), 1)
            new_comment = Comment.objects.first()
            self.assertEqual(new_comment.user, user)
            self.assertEqual(new_comment.content, payload["content"])

