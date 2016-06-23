from django.shortcuts import render, redirect
from account.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.http import Http404

# Create your views here.

def login_view(request):
    if request.user.is_authenticated():
        raise Http404

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
                    return render(request, 'login_form.html', {'login_form': login_form})
            else:
                # username/password mismatch
                messages.error(request, "Invalid username and/or password!")
                return render(request, 'login_form.html', {'login_form': login_form})
        else:
            # Form invalid
            messages.error(request, "Invalid username and/or password!")
            return render(request, 'login_form.html', {'login_form': login_form})
    else:
        # show form
        return render(request, 'login_form.html', {'login_form': login_form})



def logout_view(request):
    if not request.user.is_authenticated():
        raise Http404
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')



def register_view(request):
    if request.user.is_authenticated():
        raise Http404

    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        # submission
        if form.is_valid():
            # valid form
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # check if username or email exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken!")
                return render(request, 'register_form.html', {'form': form})
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
                return render(request, 'register_form.html', {'form': form})

            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, "Successfully registered! You can now log in!")
            return redirect('login')
        else:
            # invalid form
            messages.error(request, "Some fields are invalid!")
            return render(request, 'register_form.html', {'form': form})
    else:
        # form
        return render(request, 'register_form.html', {'form': form})