from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('sku', 'buyer', 'seller', 'channel', 'quantity', 'order_value', 'date')


admin.site.register(Order, OrderAdmin)
