from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render (request, 'home.html')

