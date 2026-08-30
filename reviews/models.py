from django.db import models
from django.utils.text import slugify
from django.conf import settings
from unidecode import unidecode
import uuid


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True

class Review (TimeStampedModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name="Название игры")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-слаг")
    content = models.TextField(verbose_name="Содержимое рецензии")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_reviews', blank=True)
    cover_image = models.ImageField(upload_to='reviews/covers/%Y/%m/', blank=True, null=True, verbose_name="Обложка")
    is_published = models.BooleanField(default=True, db_index=True, verbose_name="Опубликовано")

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = "Обзор"
        verbose_name_plural = "Обзоры"
        ordering = ['-created_at']
        
        indexes = [
            models.Index(
            fields=['author', '-created_at'],
            name='review_author_date_idx'
        ),
    ]

    def __str__(self) -> str:
        """Строковое представление объекта для интерфейсов и логов."""
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))

        super().save(*args, **kwargs)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments', verbose_name='Обзор')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    body = models.TextField(max_length=500, verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.author.username} к «{self.review.title}»'