from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.views import View
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from . import views


urlpatterns = [
    #path('getUser/',views.getUser),    
    #path('addwithphone/',views.addwithphone),
    #path('addwithgmail/',views.addwithgmail),
    #path('addwithfacebook/',views.addwithfacebook),
    #path('suggest-matches/',views.suggestmatches),
    #path('getUser/<str:pk>/',views.getUser),
    #path('right-swipe/',views.SwipeRight),
    path('admin/', admin.site.urls),
    path('login', views.login, name = "login"),
    path('logout', auth_views.LogoutView.as_view() , name = "logout"),
    path('social-auth/', include('social_django.urls', namespace='social')),
    
    path('filterUsers/', views.filterUsers),
    
]
