from django.urls import path
from .views import MenuView, CategoryView

urlpatterns = [
    path("", MenuView.as_view(), name="menu"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category_detail"),
]
