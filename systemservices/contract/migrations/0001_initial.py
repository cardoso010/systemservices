# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-01 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=200)),
                ('neighborhood', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'ordering': ('-created_at',),
            },
        ),
    ]
