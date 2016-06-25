# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20160625_0948'),
        ('products', '0004_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='repository name', max_length=50)),
                ('tel', models.PositiveIntegerField(null=True)),
                ('city', models.ForeignKey(related_name='city', verbose_name='city', to='location.City')),
            ],
        ),
        migrations.CreateModel(
            name='StoreHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(related_name='product_store', verbose_name='product', to='products.Product')),
                ('repostory', models.ForeignKey(related_name='repository', verbose_name='repository', to='store.Repository')),
            ],
        ),
    ]
