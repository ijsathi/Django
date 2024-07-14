from django.urls import path
from .views import ClassList, BookingCreate, BookingHistory

urlpatterns = [
    path('', ClassList.as_view(), name='class-list'),
    path('book/', BookingCreate.as_view(), name='class-book'),
    path('history/', BookingHistory.as_view(), name='booking-history'),
]
