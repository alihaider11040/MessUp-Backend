
import email
import math
#import geopy.distance
from datingApp.serializers import*
from datingApp.models import*
from operator import truediv

#from geopy.distance import geodesic as GD

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




from rest_framework.status import HTTP_201_CREATED
from rest_framework.request import Request
#from __future__ import print_function



from django.db.models.functions import Radians, Power, Sin, Cos, ATan2, Sqrt, Radians
from django.db.models import F



@api_view(['POST'])
def addwithphone(request): #send phone number and OTP i.e token generated for authecation
    data = request.data
    phone_number=data['phone_number']
    alreadyExists = Login.objects.filter(phone_number=phone_number).exists()
    if alreadyExists:
        user= Login.objects.get(phone_number=phone_number)
        user = Userbymobileserializer(user,many=False)
        content = {'detail': 'user already exist!', 'user-details': user.data }
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def addwithgmail(request): #send email id for authentication
    data = request.data
    email=data['email']
    alreadyExists = Login.objects.filter(email=email).exists()
    if alreadyExists:
        user= Login.objects.get(email=email)
        user = Userbymobileserializer(user,many=False)
        content = {'detail': 'user already exist!', 'user-details': user.data }
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def addwithfacebook(request): #send email id for authentication
    data = request.data
    email=data['email']
    alreadyExists = Login.objects.filter(email=email).exists()
    if alreadyExists:
        user= Login.objects.get(email=email)
        user = Userbymobileserializer(user,many=False)
        content = {'detail': 'user already exist!', 'user-details': user.data }
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getUser(request, pk):
    profile = Profile.objects.filter(id=pk).exists()
    if profile:
        serializer = ProfileSerializer(Profile.objects.GET(id=pk), many= False)
        return Response(serializer.data)
    else:
        content = {'details': 'No User exists'}
        return Response(content)


#-----not on server-------------------------#

@api_view(['POST', 'PUT'])
def SwipeRight(request):
    data = request.data
    loggedInUserID=data['person1']
    rightSwipedUserID=data['person2']
    rightSwipedAlreadyExists = MatchMake.objects.filter(person1=rightSwipedUserID).exists()
    leftSwipedAlreadyExists = MatchMake.objects.filter(person2=loggedInUserID).exists()
     
    if (rightSwipedAlreadyExists and leftSwipedAlreadyExists):
        match = MatchMake.objects.get(person1=data['person2'], person2 = data['person1'])
        match.match_check = True
        match.save()     
        matchMade = RegisterMatch(match, many=False)
        return Response(matchMade.data)
    else:
        oneSidedLike = RegisterMatch(data=request.data, many=False)
        if oneSidedLike.is_valid():
            oneSidedLike.save()
            return Response(oneSidedLike.data, status=status.HTTP_201_CREATED)




@api_view(['POST'])
def SwipeDown(request):
    data=request.data
    loggedInUserID=data['user1']
    DownSwippedUserID=data['user2']
    block_check = data['block_check']

    DownSwippedAlreadyExists = BlockProfile.objects.filter(user1=DownSwippedUserID).exists()
    loggedInAlreadyExists = BlockProfile.objects.filter(user2=loggedInUserID).exists()
    DownSwippedAlreadyExists2 = BlockProfile.objects.filter(user2=DownSwippedUserID).exists()
    loggedInAlreadyExists2 = BlockProfile.objects.filter(user1=loggedInUserID).exists()
    
    if (DownSwippedAlreadyExists and loggedInAlreadyExists) or (DownSwippedAlreadyExists2 and loggedInAlreadyExists2):
        content = {'message': 'Already Blocked'}
        return Response(content)
    else:
        BlockProfileMade = BlockProfileSerializer(data=request.data)
        if BlockProfileMade.is_valid():
            BlockProfileMade.save()
            return Response(BlockProfileMade.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def Unblock(request):
    data=request.data
    loggedInUserID=data['loggedInUserID']
    UnblockUserID=data['toBeUnblockedUserID']

    UnblockAlreadyExists = BlockProfile.objects.filter(user2=UnblockUserID).exists()
    loggedInAlreadyExists = BlockProfile.objects.filter(user1=loggedInUserID).exists()

    if loggedInAlreadyExists and UnblockAlreadyExists:
        unblockProfile = BlockProfile.objects.filter(user1= loggedInUserID, user2 = UnblockUserID).delete()
        content = {'message': 'Deleted Successfully'}
        return Response(content)
    else:
        content = {'message': 'Record does not exist'}
        return Response(content)

#SignUp Api
@api_view(['POST'])
def UserSignUpView(request):
    data=request.data
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
        #     phone_number=phone_number,
        #     token=token
        # )
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
        serializer=ADDLoginSerializer(data=request.data)
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
        user.first_name= data['FirstName']
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



#---------------------------------------------------------------------------------------------------------

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

    interests = InterestsID.objects.filter(user_id=ID)
    interestsCount = InterestsID.objects.filter(user_id=ID).count()
    
    print(interests) 
    
    i= 0
    while i < interestsCount:
        sameInterests = InterestsID.objects.filter(interest_id = interests[i].interest_id).exclude(user_id=ID)
        print(sameInterests)
        i = i+1    
    '''Get users within dist_range of longitude & Latitude'''
    dlat = Radians(F('latitude') - current_lat)
    dlong = Radians(F('longitude') - current_long)
    a = (Power(Sin(dlat/2), 2) + Cos(Radians(current_lat)) 
    * Cos(Radians(F('latitude'))) * Power(Sin(dlong/2), 2)
    )
    c = 2 * ATan2(Sqrt(a), Sqrt(1-a))
    d = 6371 * c
 
    LocationsNearMe = Profile.objects.annotate(distance=d).order_by('distance').filter(distance__lt=dist_range)
    '''filter on sexualOrientation+ageLimit+distance'''
    if qs is 'all':
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max,id__in=LocationsNearMe).exclude(id=ID)
        print("all")
    else:
        queryset = Profile.objects.filter(age__gte=age_min, age__lte=age_max,sexualOrientation__choice=qs, id__in=LocationsNearMe ).exclude(id=ID)
        #print(queryset[0].username)
        print("not all")
    serializer= filterUsersSerializer(queryset, many=True) # serialize all the objects # take objects & convert to JSON # many= true means we have many objects so DONOT stop after 1 JSON obj
    return Response(serializer.data) # return JSON response 

#-----------------------------------------------------------------------------


















# def SwipeRight(request):
#     data = request.data()
#     loggedInUserID=data['loggedInUserID']
#     #loggedInUserID=request.loggedInUserID
#     rightSwipedUserID=data['rightSwipedUserID']
#     #rightSwippedUserID=request.rightSwippedUserID
#     rightSwipedAlreadyExists = MatchMake.objects.filter(person1=rightSwipedUserID).exists()
#     leftSwipedAlreadyExists = MatchMake.objects.filter(person2=loggedInUserID).exists()
#     if rightSwipedAlreadyExists and leftSwipedAlreadyExists:
#         match = MatchMake.objects.get(person1= rightSwipedUserID, person2 = loggedInUserID)
#         match.person1 = loggedInUserID
#         match.person2 = rightSwipedUserID
#         match.match_check = True
#         match.save()
#         content = {'detail': 'Its a match'}        
#         matchMade = RegisterMatch(match, many=False)
#         return Response(matchMade.data, content)
#     else:
#         match = MatchMake.objects.create(
#             person1=data['loggedInUserID'],
#             #person1=request.loggedInUserID,
#             person2=data['rightSwipedUserID'],
#             #person2=request.rightSwippedUserID,
#             match_check=False,
#         )
#         match.save()
#         oneSidedLike = RegisterMatch(match, many=False)
#         return Response(oneSidedLike.data, status=HTTP_201_CREATED)




# @api_view(['POST'])
# def SwipeDown(request):
#     data=request.data()
#     loggedInUserID=data['loggedInUserID']
#     DownSwippedUserID=data['downSwippedUserID']

#     DownSwippedAlreadyExists = MatchMake.objects.filter(user1=DownSwippedUserID).exists()
#     loggedInAlreadyExists = MatchMake.objects.filter(user2=loggedInUserID).exists()


#     DownSwippedAlreadyExists2 = MatchMake.objects.filter(user2=DownSwippedUserID).exists()
#     loggedInAlreadyExists2 = MatchMake.objects.filter(user1=loggedInUserID).exists()
    
#     if (DownSwippedAlreadyExists and loggedInAlreadyExists) or (DownSwippedAlreadyExists2 and loggedInAlreadyExists2):
#         content = {'message': 'Already Blocked'}
#         return Response(content)
#     else:
#         block = BlockProfile.objects.create(
#             user1=data['loggedInUserID'],
#             #person1=request.loggedInUserID,
#             user2=data['rightSwippedUserID'],
#             #person2=request.rightSwippedUserID,
#             block_check=True,
#         )
#         block.save()
#         BlockProfileMade = BlockProfileSerializer(block, many=False)
#         return Response(BlockProfileMade, status=HTTP_201_CREATED)