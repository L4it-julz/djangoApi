from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

from .serializers import HeroSerializer, StockSerializer, SKUSerializer, UserSerializer
from .models import Hero, Stock, SKU, User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
   

    
class StockViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Stock.objects.all().order_by('barcode')
    serializer_class = StockSerializer
   

class SKUViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = SKU.objects.all().order_by('skuCode')
    serializer_class = SKUSerializer
    

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all().order_by('realName')
    serializer_class = UserSerializer
    