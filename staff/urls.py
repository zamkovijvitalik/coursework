from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('login/', views.staff_login, name='staff_login'),
    path('', views.staff_home, name='staff_home'),
    path('orders/', views.staff_orders, name='staff_orders'),
    path('orders/done/', views.staff_done_orders, name='done_orders'),
    path('orders/complete/<int:order_id>/', views.mark_order_completed, name='mark_order_completed'),
    path('inventory/', views.staff_inventory, name='staff_inventory'),
]
