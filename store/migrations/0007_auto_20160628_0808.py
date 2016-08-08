# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20160628_0800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storehouse',
            old_name='repository',
            new_name='repostory',
        ),
    ]
