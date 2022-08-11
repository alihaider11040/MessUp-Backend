from __future__ import print_function
#from geopy.distance import geodesic as GD
#import geopy.distance
from django.db.models.functions import Radians, Power, Sin, Cos, ATan2, Sqrt
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
from datingApp.models import InterestsID
from datingApp.serializers import InterestsSerializer

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
    '''------------------------------------------------------------------------'''
    '''Filter on location based'''
    profiles = Profile.objects.filter().exclude(id=ID)
    profilesCount = Profile.objects.filter().exclude(id=ID).count()
    #print("count:",profilesCount)

    i = 0
    dist_in_km =list()
    idsList = list()
    lats = list()
    longs = list()
    while i<profilesCount:
        profiles[i].longitude
        profiles[i].latitude

        '''Get users within dist_range of longitude & Latitude'''
        
        dlat = math.radians((profiles[i].latitude) - current_lat)
        dlong = math.radians((profiles[i].longitude) - current_long)
        
        a = (pow(math.sin(dlat/2), 2) + math.cos(math.radians(current_lat)) 
        * math.cos(math.radians(profiles[i].latitude)) * pow(math.sin(dlong/2), 2)
        )

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))        
        d = 6371 * c  # 6371 is rdaius of earth in kilometers

        if d<= float(dist_range):
            dist_in_km.append(d)
            idsList.append(profiles[i].id)

        print("dist_in_km: ",dist_in_km)
        #order_by('distance')
        #.annotate(id__in=idsList.order_by('distance').
        LocationsNearMe = Profile.objects.filter(id__in=idsList)
        #print("LocationsNearMe:", LocationsNearMe)

        i =i+1
    print("LocationsNearMe:", LocationsNearMe)
    '''------------------------------------------------------------------------'''
    '''Filter Profiles based on their Interests Matched (match if atleast 2 interests are same )'''
    interests = InterestsID.objects.filter(user_id=ID)
    interestsCount = InterestsID.objects.filter(user_id=ID).count()
    
    sameInterestsUsers = list()
    i= 0
    while i < interestsCount:
        sameInterests = InterestsID.objects.filter(interest_id = interests[i].interest_id).exclude(user_id=ID)
        sameInterestsCount = InterestsID.objects.filter(interest_id = interests[i].interest_id).exclude(user_id=ID).count()
        j = 0
        while j < sameInterestsCount:
            sameInterestsUsers.append(sameInterests[j].user_id)
            j = j+1
        i = i+1

    countCheck= 0 
    doneCheckingUsers = list()
    matchedInterestUsers = list()
    x= 0
    for x in range(len(sameInterestsUsers)):
        y = 0
        if sameInterestsUsers[x] in doneCheckingUsers:
            pass
        else:
            for y in range(len(sameInterestsUsers)):
                if sameInterestsUsers[y] == sameInterestsUsers[x]:
                    countCheck += 1
            doneCheckingUsers.append(sameInterestsUsers[x])
            if countCheck >= 2:
                matchedInterestUsers.append(sameInterestsUsers[x])
            countCheck = 0
  

    ids = Profile.objects.filter(id__in = matchedInterestUsers)

    print("ids:", ids)

    '''------------------------------------------------------------------------'''

    '''Combine Filter on ageLimit+ sexualOrientation+ distance + interests_matched'''

    if qs == 'all':
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max,id__in=idsList).filter (id__in= ids).exclude(id=ID)
        print("queryset:",queryset)
        print("all")
    else:
        '''commented part can be used later for back tracking user Profiles when Profiles r exhausted'''
        # queryset1=Profile.objects.filter(age__gte=age_min, age__lte=age_max).exclude(id=ID)
        # queryset2=Profile.objects.filter(sexualOrientation__choice=qs).exclude(id=ID)
        # print(queryset1)
        # print(queryset2)
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max,sexualOrientation__choice=qs, id__in=idsList).filter ( id__in= ids).exclude(id=ID)
        print(queryset)
        print("not all")
    serializer= filterUsersSerializer(queryset, many=True) # serialize all the objects # take objects & convert to JSON # many= true means we have many objects so DONOT stop after 1 JSON obj
    return Response(serializer.data) # return JSON response 

