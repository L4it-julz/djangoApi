from django.db.models import fields
from rest_framework import serializers
from .models import Hero, Stock, SKU, User
from api import models

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('barcode', 'stockDescription', 'unit', 'active', 'skuID')

class SKUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SKU
        fields = ('skuCode', 'skuDescription')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('realName', 'username', 'password', 'typeID', 'branchID', 'token')