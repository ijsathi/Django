from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Plan, Membership
from .serializers import PlanSerializer, MembershipSerializer
from users.permissions import IsStaff, IsMember

class PlanCreate(generics.CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsStaff]

class PlanList(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

class MembershipUpdate(generics.RetrieveUpdateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsMember]
