# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160628_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='storehouse',
            name='address',
            field=models.CharField(verbose_name='address', blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='storehouse',
            name='name',
            field=models.CharField(verbose_name='address', blank=True, max_length=50),
        ),
    ]
