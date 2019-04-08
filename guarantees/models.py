from django.db import models
from django.utils import timezone
import PIL as pillow

class Guarantees(models.Model):
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Полное описание вкладки "Гарантии"')
    is_active = models.BooleanField(default=True, verbose_name='Актуально?')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def __str__(self):
            return "%s" % self.description

    class Meta:
        verbose_name = 'Гарантии (запись)'
        verbose_name_plural = 'Гарантии (запись)'