# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0042_auto_20170109_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='backPhoto',
            field=models.ImageField(upload_to='identity', verbose_name='\u8bc1\u4ef6\u7167\u53cd\u9762 *'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='certType',
            field=models.IntegerField(default='1', help_text='\u5197\u4f59\u9879,\u4e0d\u9700\u8981\u8f93\u5165', verbose_name='\u8bc1\u4ef6\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='cvn2',
            field=models.CharField(blank=True, default='', help_text='\u5982\u679c\u662f\u4fe1\u7528\u5361\u5219\u5fc5\u987b\u586b\u5199', max_length=10, null=True, verbose_name='\u4fe1\u7528\u5361\u80cc\u9762\u7684\u672b3\u4f4d\u6570\u5b57'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='expired',
            field=models.CharField(blank=True, default='', help_text='\u5982\u679c\u662f\u4fe1\u7528\u5361\u5219\u5fc5\u987b\u586b\u5199', max_length=100, null=True, verbose_name='\u6709\u6548\u671f'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='frontPhoto',
            field=models.ImageField(upload_to='identity', verbose_name='\u8bc1\u4ef6\u7167\u6b63\u9762 *'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='originType',
            field=models.IntegerField(default='1', help_text='\u5197\u4f59\u9879,\u4e0d\u9700\u8981\u8f93\u5165', verbose_name='\u6e20\u9053\u7c7b\u578b '),
        ),
    ]
