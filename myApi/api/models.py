from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Stock(models.Model):
    barcode = models.CharField(max_length=60)
    stockDescription = models.CharField(max_length=255)
    unit = models.CharField(max_length=6)
    active = models.CharField(max_length=2)
    skuID = models.CharField(max_length=50)
    
    def __str__(self):
        return self.barcode

class SKU(models.Model):
    skuCode = models.CharField(max_length=10)
    skuDescription = models.CharField(max_length=255)

    def __str__(self):
        return self.skuCode

class User(models.Model):
    realName = models.CharField(max_length=255)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    typeID = models.CharField(max_length=2)
    branchID = models.CharField(max_length=2)
    token = models.CharField(max_length=60)

    def __str__(self):
        return self.realName

