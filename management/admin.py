from django.contrib import admin
from .models import Ingredient, PurchaseList

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "unit")
    search_fields = ("name",)

@admin.register(PurchaseList)
class PurchaseListAdmin(admin.ModelAdmin):
    list_display = ("ingredient", "quantity_needed", "created_at")
    search_fields = ("ingredient__name",)
