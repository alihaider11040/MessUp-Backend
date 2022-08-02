from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..datingApp.serializers import ProfileSerializer, Userbymobileserializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute



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
def addwithgmail(request): #send phone number and OTP i.e token generated for authecation
    data = request.data()
    phoneNumber=data['email']
    alreadyExists = Login.objects.filter(email=email).exists()
    if alreadyExists:
        content = {'detail': 'User Already Exist!'}
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            obj= serializer.save()
            return Response(obj, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def addwithfacebook(request): #send email id for authentication
    data = request.data()
    phoneNumber=data['email']
    alreadyExists = Login.objects.filter(email=email).exists()
    if alreadyExists:
        content = {'detail': 'user already exist!'}
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            obj= serializer.save()
            return Response(obj, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getUser(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many= False)
    return Response(serializer.data)







