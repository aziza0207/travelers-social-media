from django.db import models
from django.contrib.postgres.fields import ArrayField
from autoslug import AutoSlugField


class Country(models.Model):
    slug = AutoSlugField(unique=True, db_index=True)
    name = models.CharField(max_length=255, verbose_name="Название")
    top_level_domain = ArrayField(
        models.CharField(max_length=200),
        blank=True, null=True,
        verbose_name="Домен верхнего уровня",
    )
    alpha_code_iso_2 = models.CharField(max_length=255, verbose_name="Верхний код 2")
    alpha_code_iso_3 = models.CharField(max_length=255, verbose_name="Верхний код 3")
    calling_codes = ArrayField(
        ArrayField(models.CharField(max_length=200)), blank=True, null=True, verbose_name="Телефонные коды"
    )
    capital = models.CharField(max_length=255, verbose_name="Столица")
    alt_spellings = ArrayField(
        models.CharField(max_length=200),
        blank=True, null=True,
        verbose_name="Альтернативные написания",
    )
    region = models.CharField(max_length=255, verbose_name="Регион")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name_plural = "Страна"
        verbose_name = "Страны"

    def __str__(self):
        return self.name
