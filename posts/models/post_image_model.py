from django.db import models


class PostImage(models.Model):
    """Фото постов."""

    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Пост",
    )

    image = models.ImageField(
        "Фотография",
        upload_to="posts/post_image/image",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Пост - {self.post.name}, #{self.pk}"
