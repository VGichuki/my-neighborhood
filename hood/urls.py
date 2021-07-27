from django.conf.urls import url
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name ='index'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('single-hood/<id>/', views.single_hood, name='single-hood'),
    path('<id>/new-post', views.create_post, name='post'),
    path('<id>/members', views.hood_members, name='members'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/update/', views.update_profile, name='update')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)