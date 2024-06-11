from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def my_app(request):
    student = models.Student.objects.all()
    return render(request, 'my_app.html', {'data':student})

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("home")

