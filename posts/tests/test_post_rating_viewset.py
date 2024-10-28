from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import PostRating
from .factories import UserFactory
from posts.tests.factories import PostFactory


@mark.django_db
class PostRatingViewSetTest(APITestCase):
    def setUp(self):
        self.create_url: str = reverse("post-rating-create")

    def test_create_post(self):
        user = UserFactory()
        post = PostFactory()

        payload = {
            "post": post.id,
            "rating": 1,


        }
        self.client.force_login(user)
        self.assertEqual(PostRating.objects.count(), 0)
        with self.assertNumQueries(8):
            res = self.client.post(self.create_url, data=payload)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            self.assertEqual(PostRating.objects.count(), 1)
            new_rating = PostRating.objects.first()
            self.assertEqual(new_rating.user, user)
            self.assertEqual(new_rating.rating, payload["rating"])