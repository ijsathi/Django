from django.shortcuts import render, redirect
from .forms import ChangeUserInfo, RegisterForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Registered Successfully!!")
            return redirect("login")
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

class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy("profile")
    def get_success_url(self):
        return reverse_lazy("profile")
    
    def form_valid(self, form):
        messages.success(self.request, "Logged in Successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Logged in information incorrect!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data':data})

@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = ChangeUserInfo(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Updated Successfully!!")
            return redirect("profile")
    else:
        profile_form = ChangeUserInfo(instance=request.user)
    return render(request, 'update_profile.html', {'form':profile_form})


def change_password(request):
    if request.method == "POST":
        pass_change_form = PasswordChangeForm(request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request, "Password Updated Successfully!!")
            update_session_auth_hash(request, pass_change_form.user)
            return redirect("profile")
    else:
        pass_change_form = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form':pass_change_form})
