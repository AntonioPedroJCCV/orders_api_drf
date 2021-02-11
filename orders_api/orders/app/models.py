from django.db import models


class Order(models.Model):
    sku = models.CharField(max_length=100, null=False, blank=False)
    buyer = models.CharField(max_length=200, null=False, blank=False)
    seller = models.CharField(max_length=200, null=False, blank=False)
    channel = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.CharField(max_length=100, null=False, blank=False)
    order_value = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateTimeField()
