# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    
    path('add/<int:product_id>/', views.add_to_cart, name='add'),  
    
    path('', views.cart_detail, name='detail'),

    path('checkout/', views.checkout, name='checkout'),

    path('success/', views.order_success, name='success'),
    
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    
    path('update-quantity/', views.cart_update_quantity, name='cart_update_quantity'),
     
    path('history/', views.order_history, name='order_history'),
    
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),

]
