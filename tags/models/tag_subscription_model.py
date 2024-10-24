from django.db import models


class TagSubscription(models.Model):
    user = models.ForeignKey(
        "users.User",
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
