# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160723_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_required', models.BooleanField(verbose_name='Is Required', default=True)),
                ('product', models.ForeignKey(to='products.Product')),
                ('spec_val', models.ForeignKey(to='products.SpecificationValue')),
            ],
            options={
                'db_table': 'product_spec_value',
            },
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_url',
            field=models.CharField(max_length=200, null=True, verbose_name='image for product'),
        ),
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.ManyToManyField(null=True, verbose_name='specification value', through='products.ProductSpec', to='products.SpecificationValue'),
        ),
        migrations.AlterUniqueTogether(
            name='productspec',
            unique_together=set([('product', 'spec_val')]),
        ),
    ]
