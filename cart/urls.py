# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    
    path('add/<int:product_id>/', views.add_to_cart, name='add'),  
    path('', views.cart_detail, name='detail'),

    # оформлення замовлення (checkout)
    path('checkout/', views.checkout, name='checkout'),

    # сторінка успішного замовлення
    path('success/', views.order_success, name='success'),
    
]
