# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_poduct_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='poduct_detail',
            new_name='product_detail',
        ),
    ]
