from django.shortcuts import render, redirect
from account.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            messages.error(request, 'Invalid username and/or password.', extra_tags='danger')

        login(request, user)
        return redirect('home')
    context = {
        'login_form': login_form,
    }
    return render(request, 'login_form.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')