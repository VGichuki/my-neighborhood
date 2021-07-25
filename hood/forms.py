from django import forms
from .models import Neighborhood,Profile,Business,Post
from pyuploadcare.dj.forms import ImageField

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)