from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="navigation/home.html"), name="home"),
    path("menu/", TemplateView.as_view(template_name="navigation/menu.html"), name="menu"),
    path("about/", TemplateView.as_view(template_name="navigation/about.html"), name="about"),
    path("contacts/", TemplateView.as_view(template_name="navigation/contacts.html"), name="contacts"),
]
