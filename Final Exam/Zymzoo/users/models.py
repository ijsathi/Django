from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    height_ft = models.IntegerField()
    height_inch = models.IntegerField()
    weight_kg = models.FloatField()
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Update related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Update related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
