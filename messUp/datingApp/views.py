from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from datingApp.serializers import ProfileSerializer, RegisterMatch, Userbymobileserializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute
from datingApp.models import MatchMake


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
            return Response(obj, status=HTTP_201_CREATED)

def SwipeRight(request):
    data = request.data()
    loggedInUserID=data['loggedInUserID']
    #loggedInUserID=request.loggedInUserID
    rightSwippedUserID=data['rightSwippedUserID']
    #rightSwippedUserID=request.rightSwippedUserID
    rightSwippedAlreadyExists = MatchMake.objects.filter(person1=rightSwippedUserID).exists()
    leftSwippedAlreadyExists = MatchMake.objects.filter(person2=loggedInUserID).exists()
    if rightSwippedAlreadyExists and leftSwippedAlreadyExists:
        match = MatchMake.objects.get(person1= rightSwippedUserID, person2 = loggedInUserID)
        match.person1 = loggedInUserID
        match.person2 = rightSwippedUserID
        match.match_check = True
        match.save()        
        Customuser = RegisterMatch(match, many=False)
        return Response(match)
    else:
        match = MatchMake.objects.create(
            person1=data['loggedInUserID'],
            #person1=request.loggedInUserID,
            person2=data['rightSwippedUserID'],
            #person2=request.rightSwippedUserID,
            match_check=False,
        )
        match.save()
        return Response(match, status=HTTP_201_CREATED)
 


