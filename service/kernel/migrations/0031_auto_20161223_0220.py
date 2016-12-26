# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 02:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kernel', '0030_auto_20161223_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[(b'sender', b'\xe5\x8f\x91\xe9\x80\x81'), (b'receiver', b'\xe6\x8e\xa5\xe5\x8f\x97')], default=b'sender', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('type', models.CharField(choices=[(b'receipt', b'\xe6\x94\xb6\xe6\x8d\xae'), (b'borrow', b'\xe5\x80\x9f\xe6\x9d\xa1'), (b'owe', b'\xe6\xac\xa0\xe6\x9d\xa1')], default=0, max_length=100, verbose_name='\u6d88\u8d39\u7c7b\u578b')),
                ('mobile', models.CharField(default=b'', max_length=100, verbose_name='\u624b\u673a\u53f7')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u4ea4\u6613\u91d1\u989d')),
                ('summary', models.CharField(max_length=300, verbose_name='\u539f\u56e0')),
                ('make_date', models.DateTimeField(blank=True, null=True, verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
                ('receiver', models.ForeignKey(blank=True, default=b'', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, related_name='contract_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u5408\u7ea6\u8bb0\u5f55',
                'verbose_name_plural': '\u5408\u7ea6\u8bb0\u5f55',
            },
        ),
        migrations.DeleteModel(
            name='Consumption',
        ),
    ]