from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Neighborhood,Profile,Business,Post
from .forms import CreateHoodForm
from django.views.generic.base import View

# Create your views here.
def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'index.html', {'hoods': hoods})

def create_hood(request):
    if request.method == 'POST':
        form = CreateHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = CreateHoodForm()
    return render(request, 'hood.html', {'form': form})






