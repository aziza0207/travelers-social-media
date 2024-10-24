import datetime
import factory
from django.utils.timezone import now
from ..models import Tag


class TagFactory(factory.django.DjangoModelFactory):
    """Фабрика тегов"""

    name = factory.Faker("word")
    created_at = now() - datetime.timedelta(days=1)

    class Meta:
        model = Tag
