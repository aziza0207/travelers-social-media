from django.db import models
from django.conf import settings


class Comment(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="Родительский комментарий",
    )
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    content = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name_plural = "Комментарий"
        verbose_name = "Комментарии"

    def __str__(self):
        return f"Комментарий {self.content} к посту {self.post.name}"
