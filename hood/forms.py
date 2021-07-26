from django import forms
from .models import Neighborhood,Profile,Business,Post
from pyuploadcare.dj.forms import ImageField

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)

class HoodBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighborhood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')