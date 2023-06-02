from django import forms
from user import models
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя", 
        widget = forms.TextInput(
            attrs={'class': 'form-input'},
        ),
    )
    password = forms.CharField(
        label="Пароль", 
        widget = forms.PasswordInput(
            attrs={'class': 'form-input'}
        ),
    )
