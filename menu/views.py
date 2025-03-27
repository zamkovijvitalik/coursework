from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, MenuItem

class MenuView(ListView):
    model = MenuItem
    template_name = "menu/menu.html"
    context_object_name = "items"

    def get_queryset(self):
        return MenuItem.objects.filter(available=True)

class CategoryView(DetailView):
    model = Category
    template_name = "menu/category.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = MenuItem.objects.filter(category=self.object)
        return context
