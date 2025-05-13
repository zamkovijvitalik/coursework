from django.db import models
from django.conf import settings

class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    session_key   = models.CharField(max_length=40, blank=True)
    product_name  = models.CharField(max_length=100, default='', blank=True)
    product_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    quantity      = models.PositiveIntegerField(default=1)
    created_at    = models.DateTimeField(auto_now_add=True)



class Order(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
