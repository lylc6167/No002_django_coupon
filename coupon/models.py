from __future__ import unicode_literals
from django.db import models
from consumer.models import ConsumerAccount
from merchant.models import MerchantAccount


class CouponMessage(models.Model):
    serviceID = models.CharField('服务',max_length=4) #服务ID
    distritID = models.CharField('区域', max_length=3)  # 区域ID
    timelimit = models.CharField('有效期', max_length=8)  # 有效期
    typeID = models.CharField('优惠券种类',max_length=2) # 01满减02折扣03其他
    wayID = models.CharField('发行方式', max_length=2)  # 01自领取02群发
    #商户通过输入此模型生成初步券信息

class CouponPublish(models.Model):
    merchantID = models.OneToOneField(MerchantAccount.ID,on_delete=models.CASCADE) #商户ID
    message = models.ForeignKey(CouponMessage,on_delete=models.CASCADE) # 外连接上一表单
    #serviceID = models.CharField('服务',max_length=4) #服务ID
    #distritID = models.CharField('区域',max_length=3) #区域ID
    #timelimit = models.CharField('有效期',max_length=8) #有效期
    #typeID = models.ForeignKey(CouponType,on_delete=models.CASCADE) #01满减02折扣03无限制
    #系统通过此模型生成待领取券

class CouponObtain(models.Model):
    consumerID = models.OneToOneField(ConsumerAccount.ID,on_delete=models.CASCADE) #用户ID
    message = models.ForeignKey(CouponPublish,on_delete=models.CASCADE) # 外连接上一表单
    #merchantID = models.OneToOneField(MerchantAccount.ID,on_delete=models.CASCADE) # 商户ID
    #serviceID = models.CharField('服务',max_length=4) # 服务ID
    #distritID = models.CharField('区域',max_length=3) # 区域ID
    #timelimit = models.CharField('有效期',max_length=8) # 有效期
    #typeID = models.ForeignKey(CouponType,on_delete=models.CASCADE) # 01满减02折扣03红包04其他
    #消费者通过此模型领取券，并返回hashID给系统


