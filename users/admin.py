from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Додаткова інформація", {"fields": ("phone", "address", "is_manager")}),
    )
    list_display = ("username", "email", "phone", "is_manager", "is_staff", "is_superuser")
    search_fields = ("username", "email", "phone")

admin.site.register(CustomUser, CustomUserAdmin)
