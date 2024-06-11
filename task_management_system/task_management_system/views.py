from django.shortcuts import render
from task.models import TaskModel

def home(request):
    tasks = TaskModel.objects.all()
    return render(request, 'index.html', {'tasks': tasks})