from django import forms
from .models import TaskModel
from category.models import TaskCategory

class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed', 'categories']
