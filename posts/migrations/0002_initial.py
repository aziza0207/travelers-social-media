# Generated by Django 5.1.2 on 2024-10-23 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("countries", "0001_initial"),
        ("posts", "0001_initial"),
        ("tags", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="country_posts",
                to="countries.country",
                verbose_name="Страна",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, default=None, to="tags.tag"),
        ),
    ]
