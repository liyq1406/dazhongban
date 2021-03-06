# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 19:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0036_auto_20170104_0402'),
        ('trade', '0017_contract_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='payment_bank',
            field=models.CharField(default='', max_length=100, verbose_name='\u652f\u4ed8\u94f6\u884c'),
        ),
        migrations.AddField(
            model_name='contract',
            name='receipt_bank',
            field=models.CharField(default='', max_length=100, verbose_name='\u6536\u6b3e\u94f6\u884c'),
        ),
        migrations.AddField(
            model_name='contract',
            name='receiver_sign',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_receiver_sign', to='signature.Signature'),
        ),
        migrations.AddField(
            model_name='contract',
            name='sender_sign',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_sender_sing', to='signature.Signature'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contract',
            name='sender',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='contract_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
