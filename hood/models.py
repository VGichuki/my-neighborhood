from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    health_department = models.IntegerField(null=True, blank=True)
    police_department = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    logo = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.neighborhood

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=300, blank=True, default='No bio')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user

    def save_user_profile(self):
        self.save()

    @classmethod
    def get_hood_members(cls,hood):
        members=cls.objects.filter(hood__icontains=hood)
        return members

class Business(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business')
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    @classmethod
    def find_business(cls,business_id):
        found=cls.objects.get(id=business_id)
        return found

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='post_owner')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,related_name='hood_post')

    def __str__(self):
        return self.title

    



    