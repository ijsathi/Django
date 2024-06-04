from django.shortcuts import render
from django.http import HttpResponse
from . forms import contactFrom, StudentData

# Create your views here.
def my_app(req):
    return render(req, "index.html")

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        return render(request, "about.html", {'name': name, 'email': email, 'select':select })
    else:
        return render(request, "about.html")

def submit(request):
    return render(request, "form.html")
def djangoForm(request):
    if request.method == "POST":
        form = contactFrom(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./myapp/uploads/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, "django_form.html", {'form':form})
    else:
        form = contactFrom()
    return render(request, "django_form.html", {'form':form})

def studentForm(request):
    if request.method == "POST":
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, "django_form.html", {'form':form})