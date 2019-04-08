from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField(max_length=128, default=True, verbose_name='Емейл')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата подписки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Почта: %s" % self.email

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'