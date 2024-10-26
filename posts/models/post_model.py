from django.db import models
from django.conf import settings
from autoslug import AutoSlugField


class Post(models.Model):
    slug = AutoSlugField(unique=True, db_index=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_posts",
        verbose_name="Создатель",
    )

    country = models.ForeignKey(
        "countries.Country",
        on_delete=models.CASCADE,
        related_name="country_posts",
        verbose_name="Страна",
    )
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    is_visible = models.BooleanField(default=True, verbose_name="Видимый")
    tags = models.ManyToManyField("tags.Tag", default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name_plural = "Пост"
        verbose_name = "Посты"

    def __str__(self):
        return f"{self.name} от {self.author.email}"
