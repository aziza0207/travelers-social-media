from django.core.management.base import BaseCommand
import requests
from slugify import slugify
from countries.models import Country


class Command(BaseCommand):
    help = "Fetch country data from API and save it to a text file"

    def handle(self, *args, **kwargs):
        res = requests.get(
            "https://api.countrylayer.com/v2/all?access_key=a23efbcd018412271b2e0b6ee731b7e5"
        )

        if res.status_code == 200:
            data = res.json()

            countries = []

            for country_data in data:
                slug = slugify(country_data.get("name"))
                name = country_data.get("name")
                capital = country_data.get("capital")
                top_level_domain = country_data.get("topLevelDomain")
                calling_codes = country_data.get("callingCodes")
                region = country_data.get("region")
                alpha_code_iso_2 = country_data.get(
                    "alpha2Code"
                )  # ISO 3166-1 alpha-2 code
                alpha_code_iso_3 = country_data.get("alpha3Code")
                alt_spellings = country_data.get("altSpellings")

                country_instance = Country(
                    slug=slug,
                    name=name,
                    capital=capital,
                    top_level_domain=top_level_domain,
                    calling_codes=calling_codes,
                    region=region,
                    alpha_code_iso_2=alpha_code_iso_2,
                    alpha_code_iso_3=alpha_code_iso_3,
                    alt_spellings=alt_spellings,
                )

                countries.append(country_instance)
            Country.objects.bulk_create(countries)
            self.stdout.write(
                self.style.SUCCESS("Successfully fetched and saved country data.")
            )
        else:
            self.stdout.write(
                self.style.ERROR(f"Error fetching data: {res.status_code}")
            )
