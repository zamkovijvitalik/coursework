from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import CartItem, Order, OrderItem
from .forms import GuestNameForm
from cart.models import Product

def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

@require_POST
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    CartItem.objects.create(
        product=product,
        session_key=session_key,
        user=request.user if request.user.is_authenticated else None,
        quantity=1
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
