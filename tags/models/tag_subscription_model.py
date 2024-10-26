from django.db import models
from django.conf import settings


class TagSubscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_tag_subscriptions",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    tag = models.ForeignKey(
        "tags.Tag",
        related_name="tag_subscriptions",
        on_delete=models.CASCADE,
        verbose_name="Тег",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "tag"], name="unique_user_tag_subscription"
            )
        ]
        verbose_name = "Подписка на тег"
        verbose_name_plural = "Подписки на теги"

    def __str__(self):
        return f"{self.user} подписан на тег {self.tag}"
