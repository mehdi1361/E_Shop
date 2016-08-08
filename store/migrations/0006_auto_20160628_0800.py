# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160628_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storehouse',
            name='repostory',
        ),
        migrations.AddField(
            model_name='storehouse',
            name='repository',
            field=models.ForeignKey(to='store.CoRepository', default=1, related_name='repository', verbose_name='repository'),
        ),
    ]
