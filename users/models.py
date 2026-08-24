from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    avatar = models.ImageField(
        upload_to='users/avatars/%Y/%m',
        blank=True,
        null=True,
        verbose_name='Аватарка'
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='О себе'
    )

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"
