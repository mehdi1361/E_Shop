# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(verbose_name='image for product', upload_to='', null=True),
        ),
    ]
