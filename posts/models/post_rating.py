from django.db import models
from django.conf import settings
from django.db.models import UniqueConstraint


class PostRating(models.Model):
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="ratings",
        verbose_name="Пост",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    rating = models.IntegerField(
        choices=[(1, "Повысить"), (-1, "Понизить")], verbose_name="Рейтинг"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Рейтинг поста"
        verbose_name_plural = "Рейтинги постов"


    def __str__(self):
        return f"Рейтинг {self.rating} от {self.user.full_name} для поста {self.post.name}"
