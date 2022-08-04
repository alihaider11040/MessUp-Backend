from __future__ import print_function
#from geopy.distance import geodesic as GD
import geopy.distance
from django.db.models.functions import Radians, Power, Sin, Cos, ATan2, Sqrt, Radians
from django.db.models import F
import email
import math
from operator import truediv
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 #displays error if a aprticular user doesnt exist in the database
from rest_framework.views import APIView # used so that views can return API data
from rest_framework.response import Response # this gets our status or a response # returns 200 if everything good
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute
from datingApp.serializers import filterUsersSerializer

#from . models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute
#from . serializers import filterUsersSerializer

# Create your views here.

# request an API & get JSON back # so a class-based view Cab be used to inherit data from API view
# BUT we are using Function_based 
@api_view(['GET'])  #GET method to return all users with respect to age and sexual orientation
def filterUsers(request):  # we will get the age range from frontend # and sexual orientation from backend
    obj_data = request.data
    '''get all these from frontend'''
    age_min = obj_data['age_min']
    age_max = obj_data['age_max']
    ID = obj_data['ID']
    current_lat = float(obj_data['current_lat'])
    current_long = float(obj_data['current_long'])
    dist_range= obj_data['dist_range']
    
    '''check if alredy exists in DB-- if not tdisplay error404'''
    obj=get_object_or_404(Profile,id=ID)

    qs = Profile.objects.get(id=ID)
    print(qs)
    qs=qs.sexualOrientation
    print(qs)

    dlat = Radians(F('latitude') - current_lat)
    dlong = Radians(F('longitude') - current_long)

    a = (Power(Sin(dlat/2), 2) + Cos(Radians(current_lat)) 
    * Cos(Radians(F('latitude'))) * Power(Sin(dlong/2), 2)
    )

    c = 2 * ATan2(Sqrt(a), Sqrt(1-a))
    d = 6371 * c

    LocationsNearMe = Profile.objects.annotate(distance=d).order_by('distance').filter(distance__lt=dist_range)

    if qs is 'all':
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max,id__in=LocationsNearMe).exclude(id=ID)
        print("all")
    else:
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max,sexualOrientation__choice=qs, id__in=LocationsNearMe ).exclude(id=ID)
        print("not all")
    serializer= filterUsersSerializer(queryset, many=True) # serialize all the objects # take objects & convert to JSON # many= true means we have many objects so DONOT stop after 1 JSON obj
    return Response(serializer.data) # return JSON response 


#     dlat = Radians(F('latitude') - current_lat)
#     dlong = Radians(F('longitude') - current_long)

#     a = (Power(Sin(dlat/2), 2) + Cos(Radians(current_lat)) 
#     * Cos(Radians(F('latitude'))) * Power(Sin(dlong/2), 2)
#     )

#     c = 2 * ATan2(Sqrt(a), Sqrt(1-a))
#     d = 6371 * c

#     LocationsNearMe = Profile.objects.annotate(distance=d).order_by('distance').filter(distance__lt=1000)

