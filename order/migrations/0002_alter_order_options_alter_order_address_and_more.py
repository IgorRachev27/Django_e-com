# Generated by Django 4.0.3 on 2022-03-14 10:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(upload_to='media/order/image', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=16, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(max_length=10, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=1000, verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клент'),
        ),
    ]
