# Generated by Django 4.0.3 on 2022-03-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options_alter_order_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=50, verbose_name='Общая сумма заказа'),
        ),
    ]
