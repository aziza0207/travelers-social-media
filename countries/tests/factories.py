import datetime
import factory
from django.utils.timezone import now
from ..models import Country


class CountryFactory(factory.django.DjangoModelFactory):
    """Фабрика страны"""

    name = factory.Faker("country")
    capital = factory.Faker("city")
    region = factory.Faker("word")
    alpha_code_iso_2 = factory.Faker("random_uppercase_letter")
    alpha_code_iso_3 = factory.Faker("random_uppercase_letter")
    created_at = now() + datetime.timedelta(days=1)
    updated_at = now() + datetime.timedelta(days=4)

    class Meta:
        model = Country
