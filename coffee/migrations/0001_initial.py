# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeBean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bean', models.IntegerField()),
            ],
        ),
    ]
