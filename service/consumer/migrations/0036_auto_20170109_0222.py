# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0035_customuser_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcard',
            name='bank',
            field=models.CharField(blank=True, choices=[('CCB', '\u4e2d\u56fd\u5efa\u8bbe\u94f6\u884c'), ('AEON', 'AEON\u4fe1\u8d37'), ('ABC', '\u4e2d\u56fd\u519c\u4e1a\u94f6\u884c'), ('AHNX', '\u5b89\u5fbd\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('ASCCB', '\u5b89\u987a\u5e02\u5546\u4e1a\u94f6\u884c'), ('BCCARD', 'BC\u5361\u516c\u53f8'), ('BCEL', 'BCEL'), ('BCM', '\u4ea4\u901a\u94f6\u884c'), ('BEA', '\u4e1c\u4e9a\u94f6\u884c'), ('BEEB', '\u911e\u5dde\u94f6\u884c'), ('BHRCB', '\u5929\u6d25\u6ee8\u6d77\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('BJCCB', '\u5b9d\u9e21\u5e02\u5546\u4e1a\u94f6\u884c'), ('BJRCB', '\u5317\u4eac\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('BNUBANK', '\u5927\u897f\u6d0b\u94f6\u884c'), ('BOAS', '\u978d\u5c71\u94f6\u884c'), ('BOAY', '\u5b89\u9633\u94f6\u884c'), ('BOB', '\u5317\u4eac\u94f6\u884c'), ('BOBBW', '\u5e7f\u897f\u5317\u90e8\u6e7e\u94f6\u884c'), ('BOBD', '\u4fdd\u5b9a\u94f6\u884c'), ('BOC', '\u4e2d\u56fd\u94f6\u884c'), ('BOCD', '\u6210\u90fd\u94f6\u884c'), ('BOCS', '\u957f\u6c99\u94f6\u884c'), ('BOCY', '\u671d\u9633\u94f6\u884c'), ('BOCZ', '\u6ca7\u5dde\u94f6\u884c'), ('BODD', '\u4e39\u4e1c\u94f6\u884c'), ('BODL', '\u5927\u8fde\u94f6\u884c'), ('BODY', '\u5fb7\u9633\u94f6\u884c'), ('BOFS', '\u629a\u987a\u94f6\u884c'), ('BOFX', '\u961c\u65b0\u94f6\u884c'), ('BOGL', '\u6842\u6797\u94f6\u884c'), ('BOGS', '\u7518\u8083\u94f6\u884c'), ('BOGY', '\u8d35\u9633\u94f6\u884c'), ('BOGZ', '\u8d63\u5dde\u94f6\u884c'), ('BOHB', '\u9e64\u58c1\u94f6\u884c'), ('BOHH', '\u65b0\u7586\u6c47\u548c\u94f6\u884c'), ('BOHLD', '\u846b\u82a6\u5c9b\u94f6\u884c'), ('BOHRB', '\u54c8\u5c14\u6ee8\u94f6\u884c'), ('BOHS', '\u8861\u6c34\u94f6\u884c'), ('BOHX', '\u798f\u5efa\u6d77\u5ce1\u94f6\u884c'), ('BOHZ', '\u6e56\u5dde\u94f6\u884c'), ('BOIMC', '\u5185\u8499\u53e4\u94f6\u884c'), ('BOJL', '\u5409\u6797\u94f6\u884c'), ('BOJN', '\u6d4e\u5b81\u94f6\u884c'), ('BOJS', '\u664b\u5546\u94f6\u884c'), ('BOJX', '\u5609\u5174\u94f6\u884c'), ('BOKL', '\u6606\u4ed1\u94f6\u884c'), ('BOLF', '\u5eca\u574a\u94f6\u884c'), ('BOLH', '\u6f2f\u6cb3\u94f6\u884c'), ('BOLJ', '\u9f99\u6c5f\u94f6\u884c'), ('BOLY', '\u6d1b\u9633\u94f6\u884c'), ('BOLZ', '\u67f3\u5dde\u94f6\u884c'), ('BONC', '\u5357\u660c\u94f6\u884c'), ('BONX', '\u5b81\u590f\u94f6\u884c'), ('BOPDS', '\u5e73\u9876\u5c71\u94f6\u884c'), ('BOPY', '\u6fee\u9633\u94f6\u884c'), ('BOQH', '\u9752\u6d77\u94f6\u884c'), ('BOQHD', '\u79e6\u7687\u5c9b\u94f6\u884c'), ('BOQZ', '\u6cc9\u5dde\u94f6\u884c'), ('BOS', '\u4e0a\u6d77\u94f6\u884c'), ('BOSI', '\u4e2d\u94f6\u4fe1\u7528\u5361(\u56fd\u9645)\u6709\u9650\u516c\u53f8'), ('BOSJ', '\u76db\u4eac\u94f6\u884c'), ('BOSJS', '\u77f3\u5634\u5c71\u94f6\u884c'), ('BOSMX', '\u4e09\u95e8\u5ce1\u94f6\u884c'), ('BOSQ', '\u5546\u4e18\u94f6\u884c'), ('BOSR', '\u4e0a\u9976\u94f6\u884c'), ('BOSX', '\u7ecd\u5174\u94f6\u884c'), ('BOSZ', '\u82cf\u5dde\u94f6\u884c'), ('BOTL', '\u94c1\u5cad\u94f6\u884c'), ('BOTZ', '\u53f0\u5dde\u94f6\u884c'), ('BOWH', '\u4e4c\u6d77\u94f6\u884c'), ('BOXC', '\u8bb8\u660c\u94f6\u884c'), ('BOXIA', '\u897f\u5b89\u94f6\u884c'), ('BOXJ', '\u534e\u878d\u6e58\u6c5f\u94f6\u884c'), ('BOXM', '\u53a6\u95e8\u94f6\u884c'), ('BOXX', '\u65b0\u4e61\u94f6\u884c'), ('BOXY', '\u4fe1\u9633\u94f6\u884c'), ('BOYK', '\u8425\u53e3\u94f6\u884c'), ('BOZJ', '\u90d1\u5dde\u94f6\u884c'), ('BOZK', '\u5468\u53e3\u94f6\u884c'), ('BOZMD', '\u9a7b\u9a6c\u5e97\u94f6\u884c'), ('BOZZ', '\u67a3\u5e84\u94f6\u884c'), ('BSB', '\u5305\u5546\u94f6\u884c'), ('BXCCB', '\u672c\u6eaa\u5e02\u5546\u4e1a\u94f6\u884c'), ('CBD', '\u8fea\u62dc\u5546\u4e1a\u94f6\u884c'), ('CBHB', '\u6e24\u6d77\u94f6\u884c'), ('CDB', '\u627f\u5fb7\u94f6\u884c'), ('CDRCB', '\u6210\u90fd\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('CEB', '\u4e2d\u56fd\u5149\u5927\u94f6\u884c'), ('CGB', '\u5e7f\u53d1\u94f6\u884c'), ('CGSXCB', '\u91cd\u5e86\u4e09\u5ce1\u94f6\u884c'), ('CHAB', '\u957f\u5b89\u94f6\u884c'), ('CHBANK', '\u521b\u5174\u94f6\u884c'), ('CIB', '\u5174\u4e1a\u94f6\u884c'), ('CITIB', '\u82b1\u65d7\u94f6\u884c'), ('CITIC', '\u4e2d\u4fe1\u94f6\u884c'), ('CITICKW', '\u4e2d\u4fe1\u5609\u534e\u94f6\u884c\u6709\u9650\u516c\u53f8'), ('CJCCB', '\u6c5f\u82cf\u957f\u6c5f\u5546\u4e1a\u94f6\u884c'), ('CMB', '\u62db\u5546\u94f6\u884c'), ('CMBC', '\u4e2d\u56fd\u6c11\u751f\u94f6\u884c'), ('CQCB', '\u91cd\u5e86\u94f6\u884c'), ('CQRCB', '\u91cd\u5e86\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('CSC', 'CSC'), ('CSRCB', '\u5e38\u719f\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('CYBANK', '\u96c6\u53cb\u94f6\u884c'), ('CZB', '\u6d59\u5546\u94f6\u884c'), ('CZCB', '\u6d59\u6c5f\u7a20\u5dde\u94f6\u884c'), ('CZCCB', '\u957f\u6cbb\u94f6\u884c'), ('DBS', '\u661f\u5c55\u94f6\u884c'), ('DFS', '\u53d1\u73b0\u91d1\u878d\u670d\u52a1\u516c\u53f8'), ('DGCB', '\u4e1c\u839e\u94f6\u884c'), ('DRCB', '\u4e1c\u839e\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('DSBANK', '\u5927\u65b0\u94f6\u884c'), ('DTCCB', '\u5927\u540c\u5e02\u5546\u4e1a\u94f6\u884c'), ('DYCCB', '\u4e1c\u8425\u94f6\u884c'), ('DZB', '\u5fb7\u5dde\u94f6\u884c'), ('DZCCB', '\u8fbe\u5dde\u5e02\u5546\u4e1a\u94f6\u884c'), ('EGB', '\u6052\u4e30\u94f6\u884c'), ('FDB', '\u5bcc\u6ec7\u94f6\u884c'), ('FJNX', '\u798f\u5efa\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('FSSSNX', '\u4f5b\u5c71\u5e02\u4e09\u6c34\u533a\u519c\u6751\u4fe1\u7528\u5408\u4f5c\u793e'), ('GDHXCB', '\u5e7f\u4e1c\u534e\u5174\u94f6\u884c'), ('GDNX', '\u5e7f\u4e1c\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('GDNYB', '\u5e7f\u4e1c\u5357\u7ca4\u94f6\u884c'), ('GRCB', '\u5e7f\u5dde\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('GSNX', '\u7518\u8083\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('GXNX', '\u5e7f\u897f\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('GZCB', '\u5e7f\u5dde\u94f6\u884c'), ('GZNX', '\u8d35\u5dde\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('HANABANK', '\u97e9\u4e9a\u94f6\u884c'), ('HBB', '\u6cb3\u5317\u94f6\u884c'), ('HBCL', '\u6e56\u5317\u94f6\u884c'), ('HBNX', '\u6cb3\u5317\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('HDCB', '\u90af\u90f8\u94f6\u884c'), ('HKB', '\u6c49\u53e3\u94f6\u884c'), ('HKURCB', '\u6d77\u53e3\u8054\u5408\u519c\u5546\u94f6\u884c'), ('HLJNX', '\u9ed1\u9f99\u6c5f\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('HMCCB', '\u54c8\u5bc6\u5e02\u5546\u4e1a\u94f6\u884c'), ('HNNX', '\u6cb3\u5357\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('HNRCC', '\u6d77\u5357\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('HSB', '\u5fbd\u5546\u94f6\u884c'), ('HSBANK', '\u6052\u751f\u94f6\u884c'), ('HSBC', '\u6c47\u4e30\u94f6\u884c'), ('HUBNX', '\u6e56\u5317\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('HUNNX', '\u6e56\u5357\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('HXB', '\u534e\u590f\u94f6\u884c'), ('HZB', '\u676d\u5dde\u94f6\u884c'), ('IBK', '\u4f01\u4e1a\u94f6\u884c'), ('ICBC', '\u4e2d\u56fd\u5de5\u5546\u94f6\u884c'), ('JCCB', '\u664b\u57ce\u94f6\u884c'), ('JDZCCB', '\u666f\u5fb7\u9547\u5546\u4e1a\u94f6\u884c'), ('JHCCB', '\u91d1\u534e\u94f6\u884c'), ('JJCCB', '\u4e5d\u6c5f\u94f6\u884c'), ('JLNX', '\u5409\u6797\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('JNRCB', '\u6c5f\u5357\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('JSB', '\u6c5f\u82cf\u94f6\u884c'), ('JSNX', '\u6c5f\u82cf\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('JXNX', '\u6c5f\u897f\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('JYRCB', '\u6c5f\u9634\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('JZB', '\u9526\u5dde\u94f6\u884c'), ('JZCB', '\u664b\u4e2d\u94f6\u884c'), ('JZCCB', '\u7126\u4f5c\u5e02\u5546\u4e1a\u94f6\u884c'), ('KORLA', '\u5e93\u5c14\u52d2\u5e02\u5546\u4e1a\u94f6\u884c'), ('KSRCB', '\u6606\u5c71\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('LNNX', '\u8fbd\u5b81\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('LOTTE', '\u97e9\u56fd\u4e50\u5929'), ('LPSCCB', '\u516d\u76d8\u6c34\u5e02\u5546\u4e1a\u94f6\u884c'), ('LSB', '\u4e34\u5546\u94f6\u884c'), ('LSCCB', '\u4e50\u5c71\u5e02\u5546\u4e1a\u94f6\u884c'), ('LSZCCB', '\u51c9\u5c71\u5dde\u5546\u4e1a\u94f6\u884c'), ('LWB', '\u83b1\u5546\u94f6\u884c'), ('LYCB', '\u8fbd\u9633\u94f6\u884c'), ('LZCB', '\u5170\u5dde\u94f6\u884c'), ('LZCCB', '\u6cf8\u5dde\u5e02\u5546\u4e1a\u94f6\u884c'), ('MYCCB', '\u7ef5\u9633\u5e02\u5546\u4e1a\u94f6\u884c'), ('NBCB', '\u5b81\u6ce2\u94f6\u884c'), ('NBDH', '\u5b81\u6ce2\u4e1c\u6d77\u94f6\u884c'), ('NBTS', '\u5b81\u6ce2\u901a\u5546\u94f6\u884c'), ('NCB', '\u5357\u6d0b\u5546\u4e1a\u94f6\u884c'), ('NCCCB', '\u5357\u5145\u5e02\u5546\u4e1a\u94f6\u884c'), ('NHRCB', '\u5e7f\u4e1c\u5357\u6d77\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('NJCB', '\u5357\u4eac\u94f6\u884c'), ('NMGNX', '\u5185\u8499\u53e4\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('OCBC', '\u534e\u4fa8\u94f6\u884c'), ('ORDOS', '\u9102\u5c14\u591a\u65af\u94f6\u884c'), ('PAB', '\u5e73\u5b89\u94f6\u884c'), ('PJCCB', '\u76d8\u9526\u5e02\u5546\u4e1a\u94f6\u884c'), ('PSBC', '\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c'), ('PZHCCB', '\u6500\u679d\u82b1\u5e02\u5546\u4e1a\u94f6\u884c'), ('QDCCB', '\u9752\u5c9b\u94f6\u884c'), ('QDRCB', '\u9752\u5c9b\u5e02\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('QHNX', '\u9752\u6d77\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('QJCCB', '\u66f2\u9756\u5e02\u5546\u4e1a\u94f6\u884c'), ('QLB', '\u9f50\u9c81\u94f6\u884c'), ('QSB', '\u9f50\u5546\u94f6\u884c'), ('RZB', '\u65e5\u7167\u94f6\u884c'), ('SANGSUMG', '\u97e9\u56fd\u4e09\u661f\u5361\u516c\u53f8'), ('SCBL', '\u6e23\u6253\u94f6\u884c'), ('SCNX', '\u56db\u5ddd\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('SDEB', '\u987a\u5fb7\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('SDNX', '\u5c71\u4e1c\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('SHBANK', '\u65b0\u97e9\u94f6\u884c'), ('SHBB', '\u4e0a\u6d77\u5546\u4e1a\u94f6\u884c'), ('SHCARD', '\u65b0\u97e9\u5361\u516c\u53f8'), ('SHXNX', '\u9655\u897f\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('SKKB', '\u97e9\u56fd\u56fd\u6c11\u94f6\u884c'), ('SMBC', '\u65e5\u672c\u4e09\u4e95\u4f4f\u53cb\u5361\u516c\u53f8'), ('SNCCB', '\u9042\u5b81\u5e02\u5546\u4e1a\u94f6\u884c'), ('SPDB', '\u4e0a\u6d77\u6d66\u4e1c\u53d1\u5c55\u94f6\u884c'), ('SRCB', '\u4e0a\u6d77\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('SXNX', '\u5c71\u897f\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('SZRCB', '\u6df1\u5733\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('TAB', '\u6cf0\u5b89\u5e02\u5546\u4e1a\u94f6\u884c'), ('TCRCB', '\u592a\u4ed3\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('TFBANK', '\u5927\u4e30\u94f6\u884c'), ('TIBET', '\u897f\u85cf\u94f6\u884c'), ('TJCB', '\u5929\u6d25\u94f6\u884c'), ('TJRCB', '\u5929\u6d25\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('TSCCB', '\u5510\u5c71\u5e02\u5546\u4e1a\u94f6\u884c'), ('UCCB', '\u4e4c\u9c81\u6728\u9f50\u5e02\u5546\u4e1a\u94f6\u884c'), ('UNKNOW', 'Al Baraka Bank(Pakistan)'), ('UOBANK', '\u5927\u534e\u94f6\u884c'), ('WFCCB', '\u6f4d\u574a\u94f6\u884c'), ('WHBANK', '\u6c38\u4ea8\u94f6\u884c'), ('WHCCB', '\u5a01\u6d77\u5e02\u5546\u4e1a\u94f6\u884c'), ('WHNX', '\u6b66\u6c49\u5e02\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('WHRCB', '\u6b66\u6c49\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('WJRCB', '\u5434\u6c5f\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('WLBANK', '\u6c38\u9686\u94f6\u884c'), ('WOORI', '\u53cb\u5229\u94f6\u884c'), ('WXRCB', '\u65e0\u9521\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('WZCB', '\u6e29\u5dde\u94f6\u884c'), ('XJNX', '\u65b0\u7586\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('XTB', '\u90a2\u53f0\u94f6\u884c'), ('YANCCB', '\u96c5\u5b89\u5e02\u5546\u4e1a\u94f6\u884c'), ('YBCCB', '\u5b9c\u5bbe\u5e02\u5546\u4e1a\u94f6\u884c'), ('YDRCB', '\u5c71\u897f\u5c27\u90fd\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('YKYH', '\u8425\u53e3\u6cbf\u6d77\u94f6\u884c'), ('YNKMNX', '\u6606\u660e\u5e02\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('YNNX', '\u4e91\u5357\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('YQCCB', '\u9633\u6cc9\u5e02\u5546\u4e1a\u94f6\u884c'), ('YRRCB', '\u9ec4\u6cb3\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('YTCB', '\u70df\u53f0\u94f6\u884c'), ('YXCCB', '\u7389\u6eaa\u5e02\u5546\u4e1a\u94f6\u884c'), ('ZGCCB', '\u81ea\u8d21\u5e02\u5546\u4e1a\u94f6\u884c'), ('ZHHRCB', '\u73e0\u6d77\u534e\u6da6\u94f6\u884c'), ('ZHRCB', '\u73e0\u6d77\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('ZJGRCB', '\u5f20\u5bb6\u6e2f\u519c\u6751\u5546\u4e1a\u94f6\u884c'), ('ZJKCCB', '\u5f20\u5bb6\u53e3\u5e02\u5546\u4e1a\u94f6\u884c'), ('ZJMTB', '\u6d59\u6c5f\u6c11\u6cf0\u5546\u4e1a\u94f6\u884c'), ('ZJNX', '\u6d59\u6c5f\u7701\u519c\u6751\u4fe1\u7528\u793e\u8054\u5408\u793e'), ('ZJTLCB', '\u6d59\u6c5f\u6cf0\u9686\u5546\u4e1a\u94f6\u884c'), ('ZYCCB', '\u9075\u4e49\u5e02\u5546\u4e1a\u94f6\u884c'), ('DYLSCZ', '\u4e1c\u8425\u83b1\u5546\u6751\u9547\u94f6\u884c'), ('HZUB', '\u676d\u5dde\u8054\u5408\u519c\u6751\u5546\u4e1a\u94f6\u884c')], default='', max_length=50, verbose_name='\u6240\u5c5e\u94f6\u884c'),
        ),
    ]