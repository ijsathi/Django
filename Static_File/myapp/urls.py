from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.my_app, name='myapp'),
    path('about/<int:id>/', views.about, name='about'),
]
