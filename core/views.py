from django.shortcuts import render
from menu.models import MenuItem

def index(request):
    featured_items = MenuItem.objects.filter(available=True)[:6]  # Відображаємо 6 популярних позицій
    return render(request, "home.html", {"featured_items": featured_items})
