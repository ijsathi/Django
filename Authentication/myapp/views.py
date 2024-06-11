from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomAuthenticationForm, CustomPasswordChangeForm, CustomSetPasswordForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully!!")
                return redirect('login')  # Add redirect to login after successful registration
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    return redirect('profile')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
                else:
                    messages.error(request, 'Invalid username or password')
        else:
            form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Updated Successfully!!")
        else:
            form = ChangeUserData()
        return render(request, 'profile.html', {'user': request.user, 'form': form})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = CustomPasswordChangeForm(user=request.user)
        return render(request, 'change_pass.html', {'form': form})
    else:
        return redirect('login')

def pass_change_without_old_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomSetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Your password was successfully updated!')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = CustomSetPasswordForm(user=request.user)
        return render(request, 'change_pass.html', {'form': form})
    else:
        return redirect('login')

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Updated Successfully!!")
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('register')
