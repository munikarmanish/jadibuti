from django.shortcuts import render, redirect
from account.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    login_form = LoginForm(request.POST or None)
    if request.method == "POST":
        if login_form.is_valid():
            # Form valid
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # username and password match
                if user.is_active:
                    # user is active
                    login(request, user)
                    messages.success(request, "Successfully logged in!")
                    return redirect('home')
                else:
                    # user is disables
                    messages.error(request, "User is disabled!")
                    return redirect('login')
            else:
                # username/password mismatch
                messages.error(request, "Invalid username and/or password!")
                return redirect('login')
        else:
            # Form invalid
            messages.error(request, "Invalid username and/or password!")
            return redirect('login')
    else:
        return render(request, 'login_form.html', {
            'login_form': login_form,
        })

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')