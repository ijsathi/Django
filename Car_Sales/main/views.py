from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Car, Brand, Order, Comment
from .forms import CommentForm, CustomUserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.views import View

class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('car-list')
    
class UserLoginView(LoginView):
    template_name = 'login.html'
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

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        brand = self.request.GET.get('brand')
        if brand:
            return Car.objects.filter(brand__name=brand)
        return Car.objects.all()

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('car-list')
    
@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = CustomUserChangeForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Updated Successfully!!")
            return redirect("profile")
    else:
        profile_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form':profile_form})

@method_decorator(login_required, name='dispatch')
class PasswordChangeView(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'main/password_change.html', {'form': form})

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
        else:
            return render(request, 'main/password_change.html', {'form': form})

@login_required
def buy_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        order = Order(user=request.user, car=car)
        order.save()
        return redirect('order-history')
    return redirect('car-detail', pk=pk)

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})

def add_comment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.user = request.user
            comment.save()
            return redirect('car-detail', pk=pk)
    return redirect('car-detail', pk=pk)
