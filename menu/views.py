from django.shortcuts import render
from menu.models import MenuItem

def menu_view(request):
    products = MenuItem.objects.all()
    return render(request, 'menu.html', {'products': products})
