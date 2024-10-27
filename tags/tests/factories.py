import datetime
import factory
from django.utils.timezone import now
from ..models import Tag, TagSubscription
from users.tests.factories import UserFactory


class TagFactory(factory.django.DjangoModelFactory):
    """Фабрика тегов"""
    slug = factory.Sequence(lambda x: f"slug_{x}")
    name = factory.Faker("word")
    created_at = now() - datetime.timedelta(days=1)

    class Meta:
        model = Tag


class TagSubscriptionFactory(factory.django.DjangoModelFactory):
    """Фабрика подписки на теги"""

    user = factory.SubFactory(UserFactory)
    tag = factory.SubFactory(TagFactory)
    created_at = now() - datetime.timedelta(days=1)

    class Meta:
        model = TagSubscription
