from django.urls import path
from . import views
from .views import MusicianListView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView, UserRegisterView

urlpatterns = [
    # path('', views.musician_list, name='musician_list'),
    # path('musician/create/', views.musician_create, name='musician_create'),
    # path('musician/edit/<int:pk>/', views.musician_update, name='musician_update'),
    # path('musician/delete/<int:pk>/', views.musician_delete, name='musician_delete'),
    # path('album/create/', views.album_create, name='album_create'),
    # path('album/edit/<int:pk>/', views.album_update, name='album_update'),
    # path('album/delete/<int:pk>/', views.album_delete, name='album_delete'),
    
    path('', MusicianListView.as_view(), name='musician_list'),
    path('musician/create/', MusicianCreateView.as_view(), name='musician_create'),
    path('musician/edit/<int:pk>/', MusicianUpdateView.as_view(), name='musician_update'),
    path('musician/delete/<int:pk>/', MusicianDeleteView.as_view(), name='musician_delete'),
    path('album/create/', AlbumCreateView.as_view(), name='album_create'),
    path('album/edit/<int:pk>/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/delete/<int:pk>/', AlbumDeleteView.as_view(), name='album_delete'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]