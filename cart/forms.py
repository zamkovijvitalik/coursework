from django import forms

class GuestNameForm(forms.Form):
    name = forms.CharField(
        label='Ваше ім’я',
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Введіть ваше ім’я'})
    )
