from rest_framework import serializers
from coupon.models import CouponMessage, CouponPublish, CouponObtain
from No002_django_coupon import settings


class CouponMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponMessage
        fields = ('serviceID','distritID','timelimit','typeID','wayID')

class CouponPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponPublish
        fields = ('merchantID','message')

class CouponObtainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponPublish
        fields = ('consumerID', 'message')