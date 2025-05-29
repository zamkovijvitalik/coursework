from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import GuestNameForm
from .models import CartItem, Order, OrderItem
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

    for item in items:
        item.total_price = item.product.price * item.quantity

    total = sum(item.total_price for item in items)

    return render(request, 'cart/detail.html', {
        'items': items,
        'total': total,
    })


def cart_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart:detail')


@require_POST
def cart_update_quantity(request):
    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user)
    else:
        session_key = _get_session_key(request)
        items = CartItem.objects.filter(session_key=session_key)

    for item in items:
        qty = request.POST.get(f'quantities_{item.id}')
        if qty:
            try:
                item.quantity = int(qty)
                item.save()
            except ValueError:
                pass

    return redirect('cart:detail')

def checkout(request):
    if request.user.is_authenticated:
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
        return redirect('cart:order_detail', order_id=order.id)

    if request.method == 'POST':
        form = GuestNameForm(request.POST)
        if form.is_valid():
            session_key = _get_session_key(request)
            order = Order.objects.create(
                name=form.cleaned_data['name'],
                session_key=session_key)
            items = CartItem.objects.filter(session_key=session_key)
            for ci in items:
                OrderItem.objects.create(
                    order=order,
                    product=ci.product,
                    quantity=ci.quantity
                )
            items.delete()
            return redirect('cart:order_detail', order_id=order.id)
    else:
        form = GuestNameForm()

    return render(request, 'cart/checkout.html', {'form': form})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cart/order_history.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.user:
        if request.user != order.user and not request.user.is_staff:
            return redirect('cart:detail')
    else:
        session_key = _get_session_key(request)
        if order.session_key != session_key:
            return redirect('cart:detail')

    return render(request, 'cart/order_detail.html', {'order': order})

