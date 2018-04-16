from __future__ import unicode_literals
from django.db import models

class MerchantAccount(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.CharField('账户',max_length=20)
    password = models.CharField('密码',max_length=100)