# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20160628_0707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storehouse',
            options={'verbose_name': 'StoreHouse', 'verbose_name_plural': 'StoreHouses'},
        ),
        migrations.AlterField(
            model_name='corepository',
            name='name',
            field=models.CharField(verbose_name='name', max_length=50, blank=True),
        ),
    ]
