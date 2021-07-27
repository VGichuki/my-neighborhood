from django.conf.urls import url
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name ='index'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('hood/<id>/', views.hood, name='hood'),
    path('<id>/create_post/', views.create_post, name='post'),
    path('<id>/create_business/', views.create_business, name='business'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/update/', views.update_profile, name='update'),
    # path('join/<id>/', views.leave_hood, name='join'),
    # path('leave/<id>/', views.leave_hood, name='leave'),
    path('search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)