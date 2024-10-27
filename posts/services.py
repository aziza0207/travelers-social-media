from django.db.models import Q
from rest_framework.exceptions import NotFound
from .models import Post


class Service:
    model = None

    @classmethod
    def get(cls, *args, **kwargs):
        try:
            return cls.model.objects.get(*args, **kwargs)
        except cls.model.DoesNotExist:
            raise NotFound(f'{cls.model.__name__} not found')

    @classmethod
    def filter(cls, *args, **kwargs):
        return cls.model.objects.filter(*args, **kwargs)


class PostService(Service):
    model = Post

    @classmethod
    def get_subscribed_posts(cls, user):
        user_countries = user.user_country_subscriptions.values_list("country", flat=True)
        user_tags = user.user_tag_subscriptions.values_list("tag", flat=True)

        user_subscribed_users = user.subscriptions.values_list("subscribed_to", flat=True)

        subscribed_posts = cls.model.objects.filter(
            Q(country__in=user_countries) |
            Q(tags__in=user_tags) |
            Q(author__in=user_subscribed_users)
        ).exclude(author=user).select_related("country")

        return subscribed_posts
