from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Post
from .factories import UserFactory
from posts.tests.factories import PostFactory, CommentFactory
from posts.tests.factories import CountryFactory
from tags.tests.factories import TagFactory, TagSubscriptionFactory


@mark.django_db
class PostViewSetTest(APITestCase):
    def setUp(self):
        self.create_url: str = reverse("post-create")
        self.list_url: str = reverse("post-list")
        self.detail_url: str = "post-detail"
        self.subscribed_posts_url: str = reverse("subscribed-posts")

    def test_create_post(self):
        user = UserFactory()
        country = CountryFactory()
        tags = [TagFactory() for _ in range(5)]

        payload = {
            "country": country.slug,
            "name": "TestPost",
            "description": "PostDescription",
            "tags": [tag.slug for tag in tags]

        }
        self.client.force_login(user)
        self.assertEqual(Post.objects.count(), 0)
        with self.assertNumQueries(17):
            res = self.client.post(self.create_url, data=payload)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Post.objects.count(), 1)
            new_post = Post.objects.first()
            self.assertEqual(new_post.author, user)
            self.assertEqual(new_post.country.slug, payload["country"])
            self.assertEqual(new_post.name, payload["name"])
            self.assertEqual(new_post.description, payload["description"])

    def test_list_posts_as_non_authorized(self):
        posts = [
            PostFactory(is_visible=True)
            for _ in range(20)
        ]

        with self.assertNumQueries(2):
            res = self.client.get(self.list_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["count"], 10)

    def test_list_posts_subscribed(self):
        user = UserFactory()
        tags = [TagFactory() for _ in range(5)]
        tags_subscription = [TagSubscriptionFactory(user=user, tag=tag) for tag in tags]
        post = PostFactory(author=user)
        post.tags.set(tags)

        self.client.force_login(user)
        with self.assertNumQueries(3):
            res = self.client.get(self.subscribed_posts_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    @mark.skip()
    def test_post_detail(self):
        user = UserFactory()
        country = CountryFactory()
        post = PostFactory(country=country)
        comments = [CommentFactory(post=post) for _ in range(5)]

        self.client.force_login(user)
        with self.assertNumQueries(4):
            res = self.client.get(reverse(self.detail_url, kwargs={"pk": post.pk}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["name"], post.name)
        self.assertEqual(res_json["country"], post.country.name)
        self.assertEqual(len(res_json["comments"]), len(comments))

    def test_post_detail_as_non_authorized(self):
        post = PostFactory()
        with self.assertNumQueries(0):
            res = self.client.get(reverse(self.detail_url, kwargs={"pk": post.id}))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
