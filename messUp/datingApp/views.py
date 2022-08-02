from rest_framework.status import HTTP_201_CREATED, HTT
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..datingApp.serializers import ProfileSerializer, RegisterMatch, Userbymobileserializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute, MatchMake



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
def MatchMake(request): #send phone number and OTP i.e token generated for authecation
    data = request.data()
    loggedInUserID=data['loggedInUserID']
    rightSwippedUserID=data['rightSwippedUserID']
    rightSwippedAlreadyExists = MatchMake.objects.filter(person1=rightSwippedUserID).exists()
    leftSwippedAlreadyExists = MatchMake.objects.filter(person2=loggedInUserID).exists()
    if rightSwippedAlreadyExists and leftSwippedAlreadyExists:
        match = MatchMake.objects.get(person1= rightSwippedUserID, person2 = loggedInUserID)
        match.person1 = loggedInUserID
        match.person2 = rightSwippedUserID
        match.match_check = True
        match.save()        
        Customuser = RegisterMatch(match, many=False)
        return Response(match, status=HTT)
    else:
        serializer = RegisterMatch(data=request.data)
        if serializer.is_valid():
            obj= serializer.save()
            return Response(obj, status=HTTP_201_CREATED)



