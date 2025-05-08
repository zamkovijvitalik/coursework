from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(help_text="Кількість у грамах або мілілітрах")
    unit = models.CharField(max_length=20, default="г")  # г, мл, шт.

    def __str__(self):
        return f"{self.name} ({self.quantity}{self.unit})"

class PurchaseList(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_needed = models.FloatField(help_text="Необхідна кількість")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ingredient.name}: {self.quantity_needed}{self.ingredient.unit}"
