from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
import PIL as pillow

class SofaCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Наименование категории')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория мебели'
        verbose_name_plural = 'Категории мебели'

class Sofa(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=True, verbose_name='Наименование мебели')
    category = models.ForeignKey(SofaCategory, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name='Категория мебели')
    price = models.DecimalField(max_digits=10, decimal_places=0, default=True, verbose_name='Цена')
    short_description = models.TextField(max_length=50, blank=True, null=True, default=None,verbose_name='Кр. описание')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Полное описание')
    is_active = models.BooleanField(default=True, verbose_name='В наличии?')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def description_S(self):
        return truncatechars(self.description, 30)

    def __str__(self):
            return "%s" % self.name


    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'

class SofaImage(models.Model):
    Sofa = models.ForeignKey(Sofa, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Мебель')
    image = models.ImageField(upload_to='sofa_images/', verbose_name='Фотография')
    is_main = models.BooleanField(default=False, verbose_name='Главная')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
            return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография мебели'
        verbose_name_plural = 'Фотографии мебели'