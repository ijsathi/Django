from django.db import models
from users.models import User

class Class(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    schedule = models.DateTimeField()
    duration = models.DurationField()
    description = models.TextField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
