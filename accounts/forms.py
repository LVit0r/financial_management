from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput, PasswordInput, TextInput

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class LoginUser(AuthenticationForm):
    class Meta:
        email = forms.CharField(widget=EmailInput())
        password = forms.CharField(widget=TextInput())

