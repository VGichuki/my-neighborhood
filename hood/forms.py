from django import forms
import django
from .models import Neighborhood,Profile,Business,Post
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from hood import models


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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighborhood')