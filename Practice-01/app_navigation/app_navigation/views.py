from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    d = {'author':'Israt Zahan Sathi', 'id':'CSE2401031134', 'email':'ijsathi2001rs@gmail.com', 'age':22, 'hobbys':['Travelling', 'Shopping', 'Gerdening'], 'courses':[
        {
            'id':1,
            'name':'C++',
            'fee': 5000
        },
        {
            'id':2,
            'name':'Python',
            'fee': 4000
        }

    ]}
    return render(request, "home.html", d)