# Generated by Django 2.1.7 on 2019-03-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sofas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sofa',
            name='price',
            field=models.DecimalField(decimal_places=0, default=True, max_digits=10, verbose_name='Цена'),
        ),
    ]
