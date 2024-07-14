from rest_framework import serializers
from .models import Plan, Membership

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'duration', 'price']

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'user', 'plan', 'start_date', 'end_date']
