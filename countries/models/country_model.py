from django.db import models
from django.contrib.postgres.fields import ArrayField


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    top_level_domain = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        verbose_name="Домен верхнего уровня",
    )
    calling_codes = ArrayField(
        ArrayField(models.IntegerField()), blank=True, verbose_name="Телефонные коды"
    )
    capital = models.CharField(max_length=255, verbose_name="Столица")
    alt_spellings = ArrayField(
        models.CharField(max_length=200),
        blank=True, verbose_name="Альтернативные написания"
    )

    class Meta:
        verbose_name_plural = "Страна"
        verbose_name = "Страны"

    def __str__(self):
        return self.name
