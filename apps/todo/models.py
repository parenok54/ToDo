from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class ToDo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_todo',
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название таска'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Описание'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Статус операции'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    image = models.ImageField(
        upload_to='todo_images/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таски"