import datetime
import factory
from django.utils.timezone import now
from ..models import Post
from users.tests.factories import UserFactory
from countries.tests.factories import CountryFactory


class PostFactory(factory.django.DjangoModelFactory):
    """Фабрика постов"""

    slug = factory.Sequence(lambda x: f"slug_{x}")
    author = factory.SubFactory(UserFactory)
    country = factory.SubFactory(CountryFactory)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    is_visible = factory.Faker("boolean")
    created_at = now() - datetime.timedelta(days=1)

    class Meta:
        model = Post
