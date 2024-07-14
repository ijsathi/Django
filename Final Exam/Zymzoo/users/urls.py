from django.urls import path
from .views import UserCreate, UserDetail

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
