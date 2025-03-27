from django.urls import path
from .views import inventory_view, PurchaseListView

urlpatterns = [
    path("inventory/", inventory_view, name="inventory"),
    path("purchases/", PurchaseListView.as_view(), name="purchase_list"),
]
