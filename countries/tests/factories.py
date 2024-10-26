import datetime
import factory
from django.utils.timezone import now
from ..models import Country


class CountryFactory(factory.django.DjangoModelFactory):
    """Фабрика страны"""

    name = factory.Faker("country")
    capital = factory.Faker("city")
    created_at = now() + datetime.timedelta(days=1)
    updated_at = now() + datetime.timedelta(days=4)

    class Meta:
        model = Country
