from django.urls import path, include
from .views import UserRegistrationView, MembershipPlanViewSet, MemberViewSet, FitnessClassViewSet, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'membership-plans', MembershipPlanViewSet)
router.register(r'members', MemberViewSet)
router.register(r'fitness-classes', FitnessClassViewSet)
router.register(r'bookings', BookingViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]
