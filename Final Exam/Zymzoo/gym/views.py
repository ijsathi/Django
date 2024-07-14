from rest_framework import generics, viewsets
# from django.contrib.auth.models import User
from .models import MembershipPlan, Member, FitnessClass, Booking, GymUser
from .serializers import UserSerializer, MembershipPlanSerializer, MemberSerializer, FitnessClassSerializer, BookingSerializer

# User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = GymUser.objects.all()
    serializer_class = UserSerializer

class MembershipPlanViewSet(viewsets.ModelViewSet):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class FitnessClassViewSet(viewsets.ModelViewSet):
    queryset = FitnessClass.objects.all()
    serializer_class = FitnessClassSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer