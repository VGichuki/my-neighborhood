from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Neighborhood,Profile,Business,Post

# Create your views here.
def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'index.html', {'hoods': hoods})

