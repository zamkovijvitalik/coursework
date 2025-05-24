from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from cart.models import Order

SECRET_STAFF_PASSWORD = 'coffee'  # можеш винести в settings.py

def staff_login(request):
    if request.method == 'POST':
        if request.POST.get('password') == SECRET_STAFF_PASSWORD:
            request.session['staff_authenticated'] = True
            return redirect('staff:staff_home')
        else:
            return render(request, 'staff/password.html', {'error': 'Невірний пароль'})
    return render(request, 'staff/password.html')

def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('staff_authenticated'):
            return view_func(request, *args, **kwargs)
        return redirect('staff:staff_login')
    return wrapper

@staff_required
def staff_home(request):
    return render(request, 'staff/home.html')

@staff_required
def staff_orders(request):
    orders = Order.objects.filter(is_completed=False).order_by('-created_at')
    return render(request, 'staff/orders.html', {'orders': orders})

@staff_required
def staff_done_orders(request):
    orders = Order.objects.filter(is_completed=True).order_by('-created_at')
    return render(request, 'staff/done_orders.html', {'orders': orders})

@staff_required
def mark_order_completed(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_completed = True
    order.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/work/orders/'))

@staff_required
def staff_inventory(request):
    return render(request, 'staff/inventory.html')
