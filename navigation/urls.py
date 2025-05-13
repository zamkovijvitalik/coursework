from django.urls import path
from django.views.generic import TemplateView

app_name = "navigation"

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("menu/", TemplateView.as_view(template_name="menu.html"), name="menu"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("contacts/", TemplateView.as_view(template_name="contacts.html"), name="contacts"),
    path("login/", TemplateView.as_view(template_name="login.html"), name="login"),
    path("register/", TemplateView.as_view(template_name="register.html"), name="register"),
    path("account/", TemplateView.as_view(template_name="account.html"), name="account"),
]
