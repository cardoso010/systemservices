# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-12 21:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160312_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default=datetime.datetime(2016, 3, 12, 21, 12, 9, 416923, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
    ]