from django.contrib import admin
from .models import Order, OrderItem, IngredientUsage

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "status", "total_price")
    list_filter = ("status",)
    search_fields = ("user__username",)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "menu_item", "quantity", "subtotal")

@admin.register(IngredientUsage)
class IngredientUsageAdmin(admin.ModelAdmin):
    list_display = ("menu_item", "ingredient", "amount_needed")
