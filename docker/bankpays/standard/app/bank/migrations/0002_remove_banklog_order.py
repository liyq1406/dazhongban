# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 06:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banklog',
            name='order',
        ),
    ]
