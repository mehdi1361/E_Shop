# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160806_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='poduct_detail',
            field=models.TextField(verbose_name='product name', blank=True),
        ),
    ]
