# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_contractedservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractedservice',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]