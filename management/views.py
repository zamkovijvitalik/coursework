from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView
from .models import Ingredient, PurchaseList

def is_manager(user):
    return user.is_authenticated and user.is_manager

@user_passes_test(is_manager)
def inventory_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, "management/inventory.html", {"ingredients": ingredients})

class PurchaseListView(ListView):
    model = PurchaseList
    template_name = "management/purchase_list.html"
    context_object_name = "purchases"
