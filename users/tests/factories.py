import datetime
import factory
from django.utils.timezone import now
from ..models import User, UserSubscription


class UserFactory(factory.django.DjangoModelFactory):
    """Фабрика пользователей."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")

    class Meta:
        model = User


class UserSubscriptionFactory(factory.django.DjangoModelFactory):
    """Фабрика подписки пользователей"""

    subscriber = factory.SubFactory(UserFactory)
    subscribed_to = factory.SubFactory(UserFactory)
    created_at = now() - datetime.timedelta(days=1)
    updated_at = now() - datetime.timedelta(days=3)

    class Meta:
        model = UserSubscription
