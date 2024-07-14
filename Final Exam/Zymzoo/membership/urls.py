from django.urls import path
from .views import PlanCreate, PlanList, MembershipUpdate

urlpatterns = [
    path('plans/', PlanList.as_view(), name='plan-list'),
    path('plans/create/', PlanCreate.as_view(), name='plan-create'),
    path('membership/<int:pk>/', MembershipUpdate.as_view(), name='membership-update'),
]
