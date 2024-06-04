from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "myapp/home.html")
def courses(request):
    return HttpResponse("This is course page")