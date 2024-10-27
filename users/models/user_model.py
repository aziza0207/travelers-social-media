from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.manager import CustomUserManager


class User(AbstractUser):
    username = None
    image = models.ImageField(
        "Фотография",
        upload_to="users/user_image",
        blank=True,
        null=True,
    )
    email = models.EmailField(_("email address"), unique=True)
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    is_blocked = models.BooleanField(default=False, verbose_name="Заблокирован")
    is_allowed_post = models.BooleanField(default=True, verbose_name="Может ли создавать посты")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Пользователь"
        verbose_name = "Пользователи"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
