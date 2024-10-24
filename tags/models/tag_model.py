from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name_plural = "Тег"
        verbose_name = "Теги"

    def __str__(self):
        return self.name
