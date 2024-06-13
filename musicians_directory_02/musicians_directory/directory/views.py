""" from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def musician_list(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians, 'albums': albums})

def musician_create(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_create')
    else:
        form = MusicianForm()
    return render(request, 'musician_form.html', {'form': form})

def musician_update(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musician_form.html', {'form': form})

def musician_delete(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()
    return redirect('musician_list')

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})

def album_update(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('musician_list')
 """
 
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegisterForm

class MusicianListView(ListView):
    model = Album
    template_name = 'musician_list.html'
    context_object_name = 'albums'

class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

    def test_func(self):
        musician = self.get_object()
        return self.request.user == musician.user

class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    model = Musician
    template_name = 'musician_confirm_delete.html'
    success_url = reverse_lazy('musician_list')

    def test_func(self):
        musician = self.get_object()
        return self.request.user == musician.user

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician_list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.user

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('musician_list')
    
    def test_func(self):
        album = self.get_object()
        return self.request.user == album.user

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy("profile")
    def get_success_url(self):
        return reverse_lazy("musician_list")
    
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
