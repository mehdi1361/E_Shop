# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('store', '0003_auto_20160628_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoRepository',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True, verbose_name='address')),
                ('address', models.CharField(max_length=500, blank=True, verbose_name='address')),
                ('tel', models.PositiveIntegerField(null=True)),
                ('city', models.ForeignKey(verbose_name='city', related_name='city', default=1, to='location.City')),
            ],
            options={
                'verbose_name_plural': 'Repositories',
                'db_table': 'co_repository',
                'verbose_name': 'Repository',
            },
        ),
        migrations.AlterModelOptions(
            name='storehouse',
            options={'verbose_name_plural': 'Repositories', 'verbose_name': 'Repository'},
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='address',
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='city',
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='name',
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='tel',
        ),
        migrations.AddField(
            model_name='storehouse',
            name='repostory',
            field=models.ForeignKey(verbose_name='repository', related_name='repository', default=1, to='store.CoRepository'),
        ),
    ]
