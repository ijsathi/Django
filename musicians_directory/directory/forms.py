from django import forms
from .models import Musician, Album

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['musician', 'name', 'release_date', 'rating']
