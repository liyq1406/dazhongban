# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0045_auto_20170117_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='secret',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='\u6388\u6743\u7801'),
        ),
        migrations.AddField(
            model_name='identity',
            name='verify',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='\u9a8c\u8bc1\u7801'),
        ),
    ]
