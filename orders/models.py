from django.db import models
from django.conf import settings
from menu.models import MenuItem
from management.models import Ingredient

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Очікує підтвердження"),
        ("in_progress", "Готується"),
        ("completed", "Готово"),
        ("cancelled", "Скасовано"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"Замовлення {self.id} - {self.user.username} ({self.status})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        """ Автоматичний підрахунок ціни за позицію. """
        self.subtotal = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} ({self.subtotal} грн)"

class IngredientUsage(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount_needed = models.FloatField(help_text="Скільки потрібно на 1 порцію")

    def __str__(self):
        return f"{self.ingredient.name} для {self.menu_item.name} ({self.amount_needed}{self.ingredient.unit})"
