from django.db import models


class UserSubscription(models.Model):
    subscriber = models.ForeignKey(
        "users.User",
        related_name="subscriptions",
        on_delete=models.CASCADE,
        verbose_name="Подписчик",
    )
    subscribed_to = models.ForeignKey(
        "users.User",
        related_name="subscribers",
        on_delete=models.CASCADE,
        verbose_name="Подписан на",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["subscriber", "subscribed_to"], name="unique_subscription"
            )
        ]
        verbose_name = "Подписка на пользователя"
        verbose_name_plural = "Подписки на пользователей"

    def __str__(self):
        return f"{self.subscriber} подписан на {self.subscribed_to}"
