from operator import truediv
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 #displays error if a aprticular user doesnt exist in the database
from rest_framework.views import APIView # used so that views can return API data
from rest_framework.response import Response # this gets our status or a response # returns 200 if everything good
from rest_framework import status, permissions

from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute
from datingApp.serializers import filterUsersSerializer

from rest_framework.decorators import api_view, permission_classes
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


#request an API & get JSON back 
# so a class-based view Cab be used to inherit data from API view
# BUT we are using Function_based 
@api_view(['GET'])  #GET method to return all users with respect to age and sexual orientation
def filterUsers(request):  # we will get the age range from frontend # and sexual orientation from backend
    obj_data = request.data

    age_min = obj_data['age_min']
    age_max = obj_data['age_max']
    ID = obj_data['ID']
    obj=get_object_or_404(Profile,id=ID)
    # qs = Profile.objects.values_list('id', 'name') 
    # sex=qs.s
    Sexual_Orientation = Profile.objects.SexualOrientation(ID)
    # if not running then make seperate serializer for sexual orientation
    # print(Sexual_Orientation)
    obj=get_object_or_404(Profile,id=ID) 

    if SexualOrientation is 'all':
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max)
    else:
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max, SexualOrientation=Sexual_Orientation )
        serializer= filterUsers(queryset, many=True) # serialize all the objects # take objects & convert to JSON # many= true means we have many objects so DONOT stop after 1 JSON obj
        return Response(serializer.data) # return JSON response 

