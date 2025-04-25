from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import LoginForm, RegisterForm

#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def register_view(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = RegisterForm()
    return render (request, 'register.html', {'user_form': user_form})


   
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('expenses_overview')
        else:
            login_form = LoginForm()
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

      
def logout_view(request):
    logout(request)
    return redirect('login')
        