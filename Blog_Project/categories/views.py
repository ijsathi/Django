from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_category(req):
    return HttpResponse("Categories")