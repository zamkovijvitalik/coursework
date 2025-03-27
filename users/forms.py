from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True, help_text="Введіть номер телефону")
    address = forms.CharField(max_length=255, required=False, help_text="Вашу адресу (необов'язково)")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "address", "password1", "password2")
