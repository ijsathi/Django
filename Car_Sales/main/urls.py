from django.urls import path
from .views import CarListView, CarDetailView, UserRegisterView, edit_profile, buy_car, order_history, add_comment, UserLoginView, user_logout, PasswordChangeView

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', edit_profile, name='profile'),
    path('buy/<int:pk>/', buy_car, name='buy-car'),
    path('order-history/', order_history, name='order-history'),
    path('car/<int:pk>/comment/', add_comment, name='add-comment'),
    path('profile/password/', PasswordChangeView.as_view(), name='password-change'),
]
