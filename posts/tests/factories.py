import datetime
import factory
from django.utils.timezone import now
from ..models import Post, Comment, PostRating
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


class CommentFactory(factory.django.DjangoModelFactory):
    """Фабрика комментариев"""

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    content = factory.Faker("sentence")
    created_at = now() - datetime.timedelta(days=1)
    updated_at = now() - datetime.timedelta(days=1)

    class Meta:
        model = Comment


class PostRatingFactory(factory.django.DjangoModelFactory):
    """Фабрика рейтинга к посту"""

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    rating = 1
    created_at = now() - datetime.timedelta(days=1)
    updated_at = now() - datetime.timedelta(days=1)

    class Meta:
        model = PostRating
