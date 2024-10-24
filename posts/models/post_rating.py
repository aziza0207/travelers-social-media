from django.db import models
from django.db.models import UniqueConstraint


class PostRating(models.Model):
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="ratings",
        verbose_name="Пост",
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    rating = models.IntegerField(
        choices=[(1, "Повысить"), (-1, "Понизить")], verbose_name="Рейтинг"
    )

    class Meta:
        verbose_name = "Рейтинг поста"
        verbose_name_plural = "Рейтинги постов"
        constraints = [
            UniqueConstraint(fields=["post", "user"], name="unique_post_user_rating")
        ]

    def __str__(self):
        return f"Рейтинг {self.rating} от {self.user.email} для поста {self.post.name}"
