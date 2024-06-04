from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_app(req):
    data = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            "phone": "010-692-6593 x09125",
            "website": "anastasia.net",
        },
        {
            "id": 3,
            "name": "Clementine Bauch",
            "username": "Samantha",
            "email": "Nathan@yesenia.net",
            "phone": "1-463-123-4447",
            "website": "ramiro.info",
        },
        {
            "id": 4,
            "name": "Patricia Lebsack",
            "username": "Karianne",
            "email": "Julianne.OConner@kory.org",
            "phone": "493-170-9623 x156",
            "website": "kale.biz",
        }
    ]
    # Wrap the list in a dictionary
    context = {'data': data}
    return render(req, "index.html", context)

def about(request, id):
    return render(request, "about.html", {'id': id})
