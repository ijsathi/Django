from django.shortcuts import render, redirect
from .forms import ChangeUserInfo, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Registered Successfully!!")
            return redirect("register")
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form':register_form, 'type':'Register'})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, "Login Successfully!!")
                login(request, user)
                return redirect("profile")
            else:
                messages.warning(request, "Login information failed!!")
                return redirect("register")
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form':form, 'type':'Login'})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def change_user_data(request):
    if request.method == "POST":
        profile_form = ChangeUserInfo(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Updated Successfully!!")
            return redirect("profile")
    else:
        profile_form = ChangeUserInfo(instance=request.user)
    return render(request, 'profile.html', {'form':profile_form, 'type':'User Update'})