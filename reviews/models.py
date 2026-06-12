from django.db import models
from django.utils.text import slugify
from django.conf import settings
import uuid


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True

class Review (TimeStampedModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name="Название игры")
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, verbose_name="URL-слаг")
    content = models.TextField(verbose_name="Содержимое рецензии")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Обзор"
        verbose_name_plural = "Обзоры"
        ordering = ['-created_at']

    def __str__(self) -> str:
        """Строковое представление объекта для интерфейсов и логов."""
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        super().save(*args, **kwargs)