from django.db import models
from django.conf import settings


class CountrySubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_country_subscriptions",
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    country = models.ForeignKey("countries.Country", related_name="country_subscriptions", on_delete=models.CASCADE,
                                verbose_name="Страна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        verbose_name = "Подписка на страну"
        verbose_name_plural = "Подписки на страны"

    def __str__(self):
        return f"{self.user} подписан на страну {self.country.name}"
