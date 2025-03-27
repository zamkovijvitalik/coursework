from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Order, OrderItem
from menu.models import MenuItem

@login_required
def create_order(request):
    if request.method == "POST":
        order = Order.objects.create(user=request.user, total_price=0)
        total = 0

        for item_id, quantity in request.POST.items():
            if item_id.startswith("item_"):
                menu_item = MenuItem.objects.get(id=item_id.replace("item_", ""))
                subtotal = menu_item.price * int(quantity)
                OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity, subtotal=subtotal)
                total += subtotal

        order.total_price = total
        order.save()
        return redirect("order_success", order_id=order.id)

    menu_items = MenuItem.objects.filter(available=True)
    return render(request, "orders/create_order.html", {"menu_items": menu_items})

class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"
