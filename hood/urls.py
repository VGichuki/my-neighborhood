from django.conf.urls import url
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name ='index'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('single-hood/<int:id>/', views.single_hood, name='single-hood'),
    path('<hood_id>/new-post', views.create_post, name='post'),
    path('<hood_id>/members', views.hood_members, name='members'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)