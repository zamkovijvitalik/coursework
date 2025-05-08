from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import UserRegistrationForm  # Створимо форму реєстрації

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("menu")  # Після реєстрації перенаправлення
        return render(request, "users/register.html", {"form": form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("menu")
        return render(request, "users/login.html", {"form": form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("menu")
