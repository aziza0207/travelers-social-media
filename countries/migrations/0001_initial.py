# Generated by Django 5.1.2 on 2024-10-26 16:13

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "top_level_domain",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200),
                        blank=True,
                        null=True,
                        size=None,
                        verbose_name="Домен верхнего уровня",
                    ),
                ),
                (
                    "calling_codes",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=django.contrib.postgres.fields.ArrayField(
                            base_field=models.IntegerField(), size=None
                        ),
                        blank=True,
                        null=True,
                        size=None,
                        verbose_name="Телефонные коды",
                    ),
                ),
                ("capital", models.CharField(max_length=255, verbose_name="Столица")),
                (
                    "alt_spellings",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200),
                        blank=True,
                        null=True,
                        size=None,
                        verbose_name="Альтернативные написания",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
            ],
            options={
                "verbose_name": "Страны",
                "verbose_name_plural": "Страна",
            },
        ),
        migrations.CreateModel(
            name="CountrySubscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата подписки"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="country_subscriptions",
                        to="countries.country",
                        verbose_name="Страна",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подписка на страну",
                "verbose_name_plural": "Подписки на страны",
            },
        ),
    ]
