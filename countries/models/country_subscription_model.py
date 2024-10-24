from django.db import models


class CountrySubscription(models.Model):
    user = models.ForeignKey("users.User", related_name="user_country_subscriptions", on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    country = models.ForeignKey("countries.Country", related_name="country_subscriptions", on_delete=models.CASCADE,
                                verbose_name="Страна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "country"], name="unique_user_country_subscription"
            )
        ]
        verbose_name = "Подписка на страну"
        verbose_name_plural = "Подписки на страны"

    def __str__(self):
        return f"{self.user} подписан на страну {self.country.name}"
