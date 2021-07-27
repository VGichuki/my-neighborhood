from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Neighborhood,Profile,Business,Post
from .forms import CreateHoodForm,HoodBusinessForm, PostForm, CreateUserForm, UserProfileForm
# from django.views.generic.edit import DeleteView
# from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'index.html', {'hoods': hoods})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context={}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login') 
def profile(request, username):
    return render(request, 'profile.html')

@login_required(login_url='login') 
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'updateprofile.html', {'form': form})
   

@login_required(login_url='login') 
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

def single_hood(request,id):
    hood = Neighborhood.objects.get(id=id)
    if request.method =='POST':
        form = HoodBusinessForm(request.POST)
        if form.is_valid():
            business_form = form.save(commit=False)
            business_form.neighborhood = hood
            business_form.user = request.user.profile
            business_form.save()
        return redirect('index')
    else:
        form = HoodBusinessForm()
    return render(request, 'business.html', {'form': form})

@login_required(login_url='login') 
def create_post(request,id):
    hood = Neighborhood.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood')
    else:
        form = PostForm()
    return render(request, 'postform.html', {'form': form})

@login_required(login_url='login') 
def hood_members(request, id):
    hood = Neighborhood.objects.get(id=id)
    members = Profile.objects.filter(neighborhood=hood)
    return render(request, 'members.html', {'members': members})
 
# class DeleteHoodView(DeleteView):
#     model = Neighborhood
#     template_name = 'delete_hood.html'









