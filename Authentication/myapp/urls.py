from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('pass_change/', views.pass_change, name='pass_change'),
    path('pass_change_without_old_pass/', views.pass_change_without_old_pass, name='pass_change_without_old_pass'),
    path('update_profile/', views.change_user_data, name='update_profile'),
]
