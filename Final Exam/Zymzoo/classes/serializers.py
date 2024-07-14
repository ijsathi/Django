from rest_framework import serializers
from .models import Class, Booking

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'instructor', 'schedule', 'duration', 'description']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'gym_class', 'booking_date']
