from asyncio.windows_events import NULL
from email import message
from rest_framework import serializers
from django.template import RequestContext
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from datingApp.serializers import ProfileSerializer, Userbymobileserializer, ZodiacSerializer, CountrySerializer, SexualOrientationSerializer, InstituteSerializer, ProfessionSerializer, LoginSerializer,AddLoginSerializer,AddZodiacSerializer,AddProfessionSerializer,AddInstituteSerializer, AddSexualOrientationSerializer, AddCountrySerializer, AddZodiacSerializer,ADDLoginSerializer,AddProfileSerializer,GetCurrentLocationSerializer,LoginbyIDSerializer,UpdateLocationSerializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute, Country
from rest_framework import generics,mixins,viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
#from django.contrib.gis.utils import GeoIP
from .forms import UserLocationForm
from django.db import models
@api_view(['POST'])
def addwithphone(request): #send phone number and OTP i.e token generated for authecation
    data = request.data()
    phoneNumber=data['phoneNumber']
    alreadyExists = Login.objects.filter(phone_number=phoneNumber).exists()
    if alreadyExists:
        content = {'detail': 'user already exist!'}
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            obj= serializer.save()
            return Response(obj, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def UserSignUpView(request):
    data=request.data
    token=['token']
    zodiac=data['zodiac']
    username=data['username']
    first_name=data['first_name']
    last_name=data['last_name']
    bio=data['bio']
    city=data['city']
    age=data['age']
    date_of_birth=data['date_of_birth']
    gender=data['gender']
    alreadyExists = Profile.objects.filter(username=username).exists()
    if alreadyExists:
        message="already exist"
        return Response(message)
    else:
        # Login.objects.create(
        #      token=token
        #  )
        # Profession.objects.create(
        #     profession_name=profession_name
        # )
        # Institute.objects.create(
        #     institution_name=institution_name
        # )
        # SexualOrientation.objects.create(
        #     choice=choice
        # )
        # Country.objects.create(
        #     country_name=country_name
        # )
        # Zodiac.objects.create(
        #     zodiac=zodiac
        # )
        
        # Profile.objects.create(
        #  username=username,
        #  first_name=first_name, 
        #  last_name=last_name, 
        #  city=city, 
        #  bio=bio,
        #  age=age,
        #  date_of_birth=date_of_birth,
        #  gender=gender,
        #  login=login,
        #  sexualOrientation=sexualOrientation,
        #  country=country,
        #  profession=profession,
        #  institute=institute,
        #  zodiac=zodiac
        # )
        serializer=AddProfessionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            profession=serializer.save()
        serializer=AddInstituteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           institute=serializer.save()
        serializer=AddZodiacSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            zodiac=serializer.save()
        serializer=AddSexualOrientationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            sexualOrientation=serializer.save()
        serializer=AddCountrySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            country=serializer.save()
        serializer=LoginbyIDSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
             login=serializer.save()
        # serializer=AddProfileSerializer(data=data)                                                                                                                                 
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        # login=data['login']
        # zodiac=data['zodiac']
        # institute=data['institute']
        # country=data['country']
        # profession=data['profession']
        # sexualOrientation=data['sexualOrientation']
        Profile.objects.create(
         username=username,
         first_name=first_name, 
         last_name=last_name, 
         city=city, 
         bio=bio,
         age=age,
         date_of_birth=date_of_birth,
         gender=gender,
         login=login,
         sexualOrientation=sexualOrientation,
         country=country,
         profession=profession,
         institute=institute,
         zodiac=zodiac,
        )
    return Response(data)

@api_view(['POST'])
def location_on_id(request):
    data=request.data
    latitude=data['latitude']
    longitude=data['longitude']
    serializer=GetCurrentLocationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
            profession=serializer.save()
    insert_data=Profile.objects.create(
        longitude=longitude,
        latitude=latitude,
        )
    if insert_data:
            return Response(json_data)
    else:
            json_data = {'msg': "Data not saved", 'state_val': 2}
            return Response(json_data)
    return Response(data)

@api_view(['DELETE'])
def user_delete_view(request):
    data=request.data
    login=data['login']
    obj=get_object_or_404(Profile,Login)
    #UserImage.objects.filter(login=login,image=image).delete()
    content = {'detail': 'Successfully deleted'}
    return Response(content)

@api_view(['PUT'])
def user_update_view(request):
    data = request.data
    login=data['login']
    alreadyExists = Profile.objects.filter(login=login).exists()
    if alreadyExists:
        user = Profile.objects.get(login=login)
        user.first_name = data['FirstName']
        user.last_name = data['LastName']
        user.city = data['city']
        user.bio = data['bio']
        user.sexualOrientation = data['sexualOrientation']
        user.id = data['id']    
        user.country = data['country']
        user.profession = data['profession']
        user.institute = data['institute']
        user.date_of_birth = data['date_of_birth']
        user.zodiac=data['zodiac']
        user.save()
        Profile = ProfileSerializer(user, many=False)
    else:
        content = {'detail': 'user not exist'}
        return Response(content)
    return Response(Profile.data)


@api_view(['PUT','POST'])
def UpdateUserLocation(request):
    data = request.data
    id=data['id']
    alreadyExists = get_object_or_404(Login, profile__login=id)
    if alreadyExists is not NULL:
        get_object_or_404(Profile,login=id)
        user=Profile.objects.get(login=id)
        user.longitude= data['longitude']
        user.latitude= data['latitude']
        user.save()
        profile = GetCurrentLocationSerializer(user, many=False)
    return Response(profile.data)










































