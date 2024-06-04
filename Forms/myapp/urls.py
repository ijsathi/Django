from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.my_app, name='myapp'),
    path('about/', views.about, name='about'),
    path('submit_form/', views.submit, name='submit_form'),
    # path('django_form/', views.djangoForm, name='django_form'),
    path('django_form/', views.studentForm, name='django_form'),
]
