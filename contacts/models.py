from django.db import models
from django.utils import timezone
import PIL as pillow

class Contacts(models.Model):
    email = models.EmailField(max_length=128, default=True, verbose_name='Емейл')
    phone = models.CharField(max_length=18, default=True, verbose_name='Номер телефона')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Полное описание вкладки "Контакты"')
    is_active = models.BooleanField(default=True, verbose_name='Актуально?')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def __str__(self):
            return "Почта: %s, телефон: %s" % (self.email, self.phone)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'