from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        "users.User",
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

    class Meta:
        verbose_name_plural = "Пост"
        verbose_name = "Посты"

    def __str__(self):
        return self.name
