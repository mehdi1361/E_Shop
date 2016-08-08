# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='category publish time')),
                ('parent', models.ForeignKey(blank=True, to='products.Category', null=True, related_name='children')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug title')),
            ],
            options={
                'db_table': 'conditions',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='product name')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='product publish time')),
                ('created_at', models.DateTimeField(null=True, verbose_name='product created time', blank=True)),
                ('is_hidden', models.BooleanField(default=False, verbose_name='is hidden?')),
                ('is_container', models.BooleanField(default=False, verbose_name='can contain products?')),
                ('priority_manual', models.PositiveSmallIntegerField(default=0, verbose_name='manual priority')),
                ('category', models.ForeignKey(default=1, verbose_name='category', to='products.Category', on_delete=None, related_name='cateory')),
                ('parent', models.ForeignKey(blank=True, to='products.Product', null=True, related_name='children')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'products_categories',
                'verbose_name': 'Products',
                'ordering': ['id', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200, null=True, verbose_name='image for product')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publish_date')),
                ('description', models.TextField(null=True, verbose_name='description for image', blank=True)),
                ('is_enable', models.BooleanField(default=False, verbose_name='enable for show')),
                ('product', models.ForeignKey(verbose_name='product', to='products.Product', related_name='product')),
            ],
            options={
                'verbose_name_plural': 'ProductsImage',
                'db_table': 'products_images',
                'verbose_name': 'ProductsImage',
                'ordering': ['id', '-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('spec_type', models.PositiveSmallIntegerField(default=1, verbose_name='spec type', choices=[(1, 'type1'), (2, 'type2'), (3, 'type3')])),
            ],
            options={
                'db_table': 'specs',
            },
        ),
        migrations.CreateModel(
            name='SpecificationValue',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('display_value', models.CharField(max_length=150, verbose_name='display value')),
                ('slug', models.SlugField(help_text='Use ascii characters', verbose_name='slug value', blank=True)),
                ('is_filter_option', models.BooleanField(default=False, help_text='If marked this value will be available for search filtering', verbose_name='Display for filtering?')),
                ('specification', models.ForeignKey(to='products.Specification', verbose_name='Specification')),
            ],
            options={
                'db_table': 'specs_values',
                'ordering': ['specification_id', 'id'],
            },
        ),
    ]
