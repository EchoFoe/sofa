from django.db import models
from django.utils import timezone
import PIL as pillow

class About_us(models.Model):
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Полное описание кладки "О компании"')
    is_active = models.BooleanField(default=True, verbose_name='Актуально?')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def __str__(self):
            return "%s" % self.description

    class Meta:
        verbose_name = 'О компании (запись)'
        verbose_name_plural = 'О компании (запись)'

class About_usImage(models.Model):
    About_us = models.ForeignKey(About_us, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='О компании')
    image = models.ImageField(upload_to='about_us_images/', verbose_name='Фотография')
    is_main = models.BooleanField(default=False, verbose_name='Главная')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
            return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография к вкладке "О компании"'
        verbose_name_plural = 'Фотографии к вкладкам "О компании"'