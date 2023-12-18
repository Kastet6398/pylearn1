from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Ім'я користувача", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'password'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Ім'я користувача")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Електронна пошта")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Ім'я")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Прізвище")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Повторення паролю")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')