# Generated by Django 2.1.7 on 2019-03-29 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='message',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='middle_name',
        ),
    ]