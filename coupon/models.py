from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from consumer.models import ConsumerAccount
from merchant.models import MerchantAccount


class CouponMessage(models.Model):
    serviceID = models.CharField('服务',max_length=4) #服务ID
    distritID = models.CharField('区域', max_length=4)  # 区域ID
    start_date = models.DateTimeField('起始日期', default=timezone.now)  # 领取时间
    end_date = models.DateTimeField('终止日期', auto_now=True)  # 使用期限限定在一定时间内，超时失效
    typeID = models.CharField('优惠券种类',max_length=2) # 01满减02折扣03其他
    wayID = models.CharField('发行方式', max_length=2)  # 01自领取02群发
    number = models.PositiveSmallIntegerField('发行数量')  # [0,32767]一般不会超范围
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
    #消费者通过系统领取券，并返回hashID给此模型


