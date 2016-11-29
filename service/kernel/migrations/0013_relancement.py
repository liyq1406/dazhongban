# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0012_merge_20161128_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relancement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='\u516c\u544a\u6807\u9898')),
                ('content', models.CharField(default='', max_length=200, verbose_name='\u516c\u544a\u5185\u5bb9')),
                ('price', models.ImageField(blank=True, height_field='url_height', help_text='\u56fe\u7247\u5c3a\u5bf8\u6700\u597d\u4e3a75x75', null=True, upload_to='goods', verbose_name='\u56fe\u7247', width_field='url_width')),
                ('applicant', models.CharField(default='', max_length=50, verbose_name='\u7533\u8bf7\u4eba')),
                ('creation_time', models.DateField(auto_now_add=True, verbose_name='\u7533\u8bf7\u65f6\u95f4\uff0c\u7cfb\u7edf\u81ea\u5efa')),
                ('approval', models.CharField(default='', max_length=50, verbose_name='\u5ba1\u6279\u4eba')),
                ('operation', models.CharField(choices=[('1', '\u5168\u90e8\u64cd\u4f5c\u7cfb\u7edf\u7c7b\u578b'), ('2', 'IOS\u7cfb\u7edf'), ('3', 'Android\u7cfb\u7edf')], max_length=10, verbose_name='\u7528\u6237\u64cd\u4f5c\u7cfb\u7edf\u9650\u5236')),
                ('gender', models.CharField(choices=[('1', '\u5168\u90e8\u6027\u522b'), ('2', '\u7537\u6027\u7528\u6237'), ('3', '\u5973\u6027\u7528\u6237')], max_length=10, verbose_name='\u7528\u6237\u6027\u522b\u9650\u5236')),
                ('age', models.CharField(choices=[('1', '\u5168\u90e8\u5e74\u9f84\u5c42'), ('2', '20~40\u5c81\u7528\u6237'), ('3', '40~60\u5c81\u7528\u6237'), ('4', '60\u5c81\u4ee5\u4e0a\u7528\u6237')], max_length=10, verbose_name='\u7528\u6237\u5e74\u9f84\u9650\u5236')),
                ('authentication', models.CharField(choices=[('1', '\u5168\u90e8\u8ba4\u8bc1\u65b9\u5f0f'), ('2', 'A \u7c7b\u8ba4\u8bc1'), ('3', 'B \u7c7b\u8ba4\u8bc1'), ('4', 'C \u7c7b\u8ba4\u8bc1'), ('5', 'D \u7c7b\u8ba4\u8bc1')], max_length=10, verbose_name='\u7528\u6237\u8ba4\u8bc1\u7c7b\u578b')),
                ('certificates', models.CharField(choices=[('1', '\u5168\u90e8\u8ba4\u8bc1\u7c7b\u578b'), ('2', '\u8eab\u4efd\u8bc1'), ('3', '\u62a4\u7167'), ('4', '\u519b\u5b98\u8bc1'), ('5', '\u53f0\u80de\u8bc1')], max_length=10, verbose_name='\u7528\u6237\u8bc1\u4ef6\u7c7b\u578b')),
                ('approval_status', models.CharField(choices=[('1', '\u5f85\u5ba1\u6838'), ('2', '\u5df2\u53d1\u5e03'), ('3', '\u5df2\u9a73\u56de')], default='1', max_length=10, verbose_name='\u5ba1\u6279\u72b6\u6001')),
                ('applicant_time', models.DateTimeField(auto_now=True, verbose_name='\u5ba1\u6279\u65f6\u95f4')),
                ('order', models.IntegerField(default='1', verbose_name='\u6392\u5e8f')),
            ],
            options={
                'verbose_name': '\u521b\u5efa\u516c\u544a',
                'verbose_name_plural': '\u521b\u5efa\u516c\u544a',
            },
        ),
    ]