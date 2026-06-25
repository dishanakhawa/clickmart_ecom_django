from django.contrib import admin
from .models import Cart, CartItem
# from models it is imported

# class CartItemAdmin(admin.ModelAdmin):
#   list_display = ['cart','product','qunatity']

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)