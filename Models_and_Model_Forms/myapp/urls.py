from django.urls import path
from . import views
urlpatterns = [
    path('', views.my_app, name='home'),
    path('delete/<int:roll>', views.delete_student, name='delete_student'),
]
