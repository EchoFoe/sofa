# Generated by Django 2.1.7 on 2019-04-08 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=True, max_length=128, verbose_name='Емейл')),
                ('phone', models.CharField(default=True, max_length=18, verbose_name='Номер телефона')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Полное описание вкладки "Гарантии"')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуально?')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания записи')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата редактирования записи')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
