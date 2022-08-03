from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.views import View
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    #path('accounts/', include('allauth.urls')),
    #path('auth/', include('rest_auth.urls')),
    #path('auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('login', views.login, name = "login"),
    path('logout', auth_views.LogoutView.as_view() , name = "logout"),
    path('social-auth/', include('social_django.urls', namespace='social')),
    
    path('filterUsers/', views.filterUsers),
    
    path("", views.home, name= "home") 
]