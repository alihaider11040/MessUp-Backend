from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from django.contrib.auth import views as auth_views
from datingApp import views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('datingApp.urls')),
]