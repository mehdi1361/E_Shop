# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_auto_20160628_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time for factor')),
                ('is_confirm', models.BooleanField(verbose_name='confirm factor', default=False)),
                ('confirm_time', models.DateTimeField(verbose_name='created time for factor', auto_now=True)),
                ('is_send', models.BooleanField(verbose_name='send factor', default=False)),
                ('send_time', models.DateTimeField(verbose_name='send time for factor', auto_now=True)),
                ('repository', models.ForeignKey(default=1, verbose_name='factor for repository', to='store.CoRepository')),
                ('user', models.ForeignKey(default=1, verbose_name='factor user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'factor',
                'verbose_name': 'facror',
                'verbose_name_plural': 'facrors',
            },
        ),
        migrations.CreateModel(
            name='ProductFactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('factor', models.ForeignKey(related_name='factor', verbose_name='factor', to='store.Factor')),
                ('store', models.ForeignKey(related_name='store', verbose_name='store', to='store.StoreHouse')),
            ],
            options={
                'db_table': 'product_factor_history',
                'verbose_name': 'product in facror',
                'verbose_name_plural': 'products in factor',
            },
        ),
    ]
