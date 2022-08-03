from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from datingApp.serializers import ProfileSerializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute
from rest_framework import generics,mixins,viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

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
    login=data['login']
    serializer=ProfileSerializer(data=request.data)                                                                                                                                 
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        alreadyExists = Profile.objects.filter(login=login).exists()
        if alreadyExists:
            #serializer=UserImagesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                obj=Profile.objects.get(login=login)
                data=ProfileSerializer(many=False).data
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



