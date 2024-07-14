from django.db import models
from users.models import User

class Plan(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.plan:
            self.end_date = self.start_date + timedelta(days=self.plan.duration)
        super().save(*args, **kwargs)
