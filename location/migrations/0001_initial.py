# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='city name')),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug city')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='insert time')),
            ],
            options={
                'verbose_name_plural': 'cities',
                'db_table': 'city',
                'verbose_name': 'cities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='state name')),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug state')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='insert time')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'db_table': 'country',
                'verbose_name': 'countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='state name')),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug state')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='insert time')),
                ('country', models.ForeignKey(verbose_name='country', to='location.Country', on_delete=None, related_name='country')),
            ],
            options={
                'verbose_name_plural': 'states',
                'db_table': 'state',
                'verbose_name': 'states',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(verbose_name='state', to='location.State', on_delete=None, related_name='state'),
        ),
    ]
