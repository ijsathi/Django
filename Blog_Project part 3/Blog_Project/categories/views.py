from django.shortcuts import render, redirect
from . import forms
from .models import Category

# Create your views here.
def add_category(request):
    if request.method == "POST":
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_name = category_form.cleaned_data['name']
            if not Category.objects.filter(name=category_name).exists():
                category_form.save()
                return redirect("add_category")
            else:
                # Category with the same name already exists
                alert_message = "Category with this name already exists."
                return render(request, "add_category.html", {'form': category_form, 'alert_message': alert_message})
                pass
    else:
        category_form = forms.CategoryForm()
    return render(request, "add_category.html", {'form':category_form})
