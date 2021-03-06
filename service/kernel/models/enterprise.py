# coding:utf-8
from __future__ import unicode_literals

import datetime

from django.db import models

from service.kernel.contrib.utils.hashlib import md5, sha1

BANK_ACCOUNTYPE = (
    ('0', '对公银行账户'),
    ('1', '对私银行账户'),
)
BANK_ACCOUNT = (
    ('0', '工商银行'),
    ('1', '农业银行'),
    ('2', '建设银行'),
    ('3', '中国银行'),
    ('4', '中信实业银行'),
    ('5', '恒丰银行'),
    ('6', '广东发展银行'),
    ('7', '深圳发展银行'),
    ('8', '光大银行'),
)


class EnterpriseUser(models.Model):
    enterprise_name = models.CharField(max_length=100, verbose_name=u'企业名称')
    bank_accountType = models.CharField(verbose_name=u'银行账户类型', choices=BANK_ACCOUNTYPE, max_length=100, default=0)
    bank_accountName = models.CharField(verbose_name=u'银行开户名', max_length=100)
    bank_num = models.IntegerField(verbose_name=u'银行账号')
    bank_account = models.CharField(verbose_name=u'开户银行', max_length=100, choices=BANK_ACCOUNT, default=0)
    bank_add = models.CharField(verbose_name=u'开户银行所在地', max_length=100)
    bank_branch = models.CharField(verbose_name=u'开户银行支行名称', max_length=200)
    yesterday_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'昨日收入总计')
    platform_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'平台收入总计')
    settled_date = models.DateTimeField(auto_now=True, verbose_name=u'入驻时间')
    appkey = models.CharField(verbose_name=u'APPKEY', max_length=100, blank=True, null=True)
    secret = models.CharField(verbose_name=u'SECRET', max_length=200, blank=True, null=True)
    callback = models.URLField(verbose_name=u'回调URL', blank=True, null=True)

    def __unicode__(self):
        return self.enterprise_name

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        self.appkey = md5(self.bank_account).hexdigest()
        self.secret = sha1(str(datetime.datetime.now())).hexdigest()
        super(EnterpriseUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = (u'企业用户')
        verbose_name_plural = (u'企业用户')
