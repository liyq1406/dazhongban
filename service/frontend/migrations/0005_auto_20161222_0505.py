# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_remove_qrtoken_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrtoken',
            name='created',
        ),
        migrations.RemoveField(
            model_name='qrtoken',
            name='modified',
        ),
        migrations.AddField(
            model_name='qrtoken',
            name='raw',
            field=models.TextField(default=0, verbose_name='\u539f\u59cb\u6570\u636e'),
            preserve_default=False,
        ),
    ]
