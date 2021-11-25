from django.contrib import admin
from .models import Hero, Stock, SKU, User

admin.site.register(Hero)
admin.site.register(Stock)
admin.site.register(SKU)
admin.site.register(User)