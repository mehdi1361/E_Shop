# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='repository name', max_length=50)),
                ('tel', models.PositiveIntegerField(null=True)),
                ('city', models.ForeignKey(related_name='city', verbose_name='city', to='location.City')),
            ],
            options={
                'db_table': 'repository',
                'verbose_name': 'Repository',
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.CreateModel(
            name='StoreHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(related_name='product_store', verbose_name='product', to='products.Product')),
                ('repostory', models.ForeignKey(related_name='repository', verbose_name='repository', to='store.Repository')),
            ],
            options={
                'db_table': 'store_house',
            },
        ),
    ]
