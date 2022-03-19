# Generated by Django 4.0.3 on 2022-03-12 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название подкатегории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/product', verbose_name='Изображение товара')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Категория')),
                ('sub_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
