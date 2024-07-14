from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Class, Booking
from .serializers import ClassSerializer, BookingSerializer
from users.permissions import IsMember

class ClassList(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]

class BookingCreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsMember]

class BookingHistory(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsMember]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
