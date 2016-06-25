# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(choices=[(1, 'type1'), (2, 'type2'), (3, 'type3')], verbose_name='repository name', max_length=50),
        ),
        migrations.AlterModelTable(
            name='repository',
            table='repository',
        ),
    ]
