# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    # показати вміст кошика
    path('', views.cart_detail, name='detail'),

    # додати товар у кошик
    path('add/<int:pk>/', views.add_to_cart, name='add'),

    # оформлення замовлення (checkout)
    path('checkout/', views.checkout, name='checkout'),

    # сторінка успішного замовлення
    path('success/', views.order_success, name='success'),
]
