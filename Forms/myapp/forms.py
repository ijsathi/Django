from typing import Any
from django import forms
from django.core import validators
import datetime

class contactFrom(forms.Form):
    name = forms.CharField(label='User Name', initial='XYZ', required=False, help_text='must be 50', widget=forms.Textarea)
    file = forms.FileField() 
    # email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    bithday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICE = [("S", "Small"), ("M", "Medium"), ("L", "Lerge")]
    size = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
    CHOICE2 = [("S", "Small"), ("M", "Medium"), ("L", "Lerge")] 
    options = forms.MultipleChoiceField(choices=CHOICE2, widget=forms.CheckboxSelectMultiple)
    check = forms.BooleanField()
    
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")
    
class StudentData(forms.Form):
    name =forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name at least 10 characters')])
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    # email = forms.EmailField()
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email =forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid Email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),validators.MinValueValidator(24, message="age must be at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message = 'File Extension must be ended with .pdf')])
    day = forms.DateField(initial=datetime.date.today)
    agree = forms.BooleanField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)