from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import CartItem, Order, OrderItem
from .forms import GuestNameForm
from menu.models import MenuItem

def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

@require_POST
def add_to_cart(request, pk):
    # Жорсткий хардкод-словник товарів
    MENU = {
        1: {'name':'Americano', 'price':60},

        # …додай решту
    }
    data = MENU.get(pk)
    if not data:
        raise Http404("Невідомий товар")
    if request.user.is_authenticated:
        user_field = {'user': request.user}
    else:
        user_field = {'session_key': _get_session_key(request)}
    CartItem.objects.create(
        product_name  = data['name'],
        product_price = data['price'],
        **user_field
    )
    return redirect('cart:detail')


def cart_detail(request):
    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user)
    else:
        session_key = _get_session_key(request)
        items = CartItem.objects.filter(session_key=session_key)
    return render(request, 'cart/detail.html', {'items': items})

def checkout(request):
    if request.user.is_authenticated:
        # авторизований користувач: створюємо без форми
        order = Order.objects.create(
            name=request.user.get_full_name() or request.user.username,
            user=request.user
        )
        items = CartItem.objects.filter(user=request.user)
        for ci in items:
            OrderItem.objects.create(
                order=order,
                product=ci.product,
                quantity=ci.quantity
            )
        items.delete()
        return redirect('cart:success')

    # гостьовий чек-аут
    if request.method == 'POST':
        form = GuestNameForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(name=form.cleaned_data['name'])
            session_key = _get_session_key(request)
            items = CartItem.objects.filter(session_key=session_key)
            for ci in items:
                OrderItem.objects.create(
                    order=order,
                    product=ci.product,
                    quantity=ci.quantity
                )
            items.delete()
            return redirect('cart:success')
    else:
        form = GuestNameForm()
    return render(request, 'cart/checkout.html', {'form': form})

def order_success(request):
    return render(request, 'cart/success.html')
