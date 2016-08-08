# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.PositiveIntegerField(verbose_name='price for product', default=0)),
                ('discount', models.PositiveIntegerField(verbose_name='discount for product', default=0)),
                ('is_enable', models.BooleanField(verbose_name='enable?', default=True)),
                ('product', models.ForeignKey(default=1, related_name='product_price', verbose_name='product', to='products.Product')),
            ],
            options={
                'db_table': 'product_price_history',
                'verbose_name': 'Price History',
                'verbose_name_plural': 'Price History',
            },
        ),
    ]
