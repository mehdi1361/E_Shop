# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='city',
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='repostory',
        ),
        migrations.AddField(
            model_name='storehouse',
            name='city',
            field=models.ForeignKey(related_name='city', to='location.City', default=1, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='storehouse',
            name='tel',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Repository',
        ),
    ]
