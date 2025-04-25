from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome de usuário'
        })
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )


class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(
        required=True,
        label='E-mail',
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail', 'class': 'form-control'})
    )
    
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'})
    )
    
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Digite seu nome de usuário', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Digite seu nome', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Digite seu sobrenome', 'class': 'form-control'}),
        }
