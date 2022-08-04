from email import message
import requests
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from datingApp.serializers import ProfileSerializer, RegisterMatch, Userbymobileserializer, BlockProfileSerializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute
from datingApp.models import MatchMake, BlockProfile
from rest_framework import status


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


@api_view(['POST'])
def addwithgmail(request): #send email id for authentication
    data = request.data()
    email=data['email']
    alreadyExists = Login.objects.filter(email=email).exists()
    if alreadyExists:
        content = {'detail': 'User Already Exist!'}
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            obj= serializer.save()
            return Response(obj, status=HTTP_201_CREATED)

@api_view(['POST'])
def addwithfacebook(request): #send email id for authentication
    data = request.data()
    email=data['email']
    alreadyExists = Login.objects.filter(email=email).exists()
    if alreadyExists:
        content = {'detail': 'user already exist!'}
        return Response(content)
    else:
        serializer = Userbymobileserializer(data=request.data)
        if serializer.is_valid():
            obj= serializer.save()
            return Response(obj, status=HTTP_201_CREATED)


@api_view(['GET'])
def getUser(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many= False)
    return Response(serializer.data)

@api_view(['POST'])
def SwipeRight(request):
    data = request.data
    loggedInUserID=data['person1']
    rightSwipedUserID=data['person2']
    rightSwipedAlreadyExists = MatchMake.objects.filter(person1=rightSwipedUserID).exists()
    leftSwipedAlreadyExists = MatchMake.objects.filter(person2=loggedInUserID).exists()

    rightSwipedAlreadyExists2 = MatchMake.objects.filter(person2=rightSwipedUserID).exists()
    leftSwipedAlreadyExists2 = MatchMake.objects.filter(person1=loggedInUserID).exists()
     
    if (rightSwipedAlreadyExists and leftSwipedAlreadyExists) or (rightSwipedAlreadyExists2 and leftSwipedAlreadyExists2):
        match = MatchMake.objects.get(person1=data['person2'], person2 = data['person2'])
        match.person1 = data['person1']
        match.person2 = data['person2']
        match.match_check = True
        match.save()
        content = {'detail': 'Its a match'}        
        matchMade = RegisterMatch(match, many=False)
        return Response(matchMade.data, content)
    else:
        oneSidedLike = RegisterMatch(data=request.data, many=False)
        if oneSidedLike.is_valid():
            oneSidedLike.save()
            return Response(oneSidedLike.data, status=status.HTTP_201_CREATED)

api_view(['PUT'])
def updateMatchMake(request):
    data = request.data
    match = MatchMake.objects.get(person1=data['person1'], person2 = data['person2'])
    match.person1 = data['person1']
    match.person2 = data['person2']
    match.match_check = True
    match.save()
    content = {'detail': 'Its a match'}        
    matchMade = RegisterMatch(match, many=False)
    return Response(matchMade.data, content)

api_view(['POST'])
def newMatchRecord(request):
    oneSidedLike = RegisterMatch(data=request.data, many=False)
    if oneSidedLike.is_valid():
        oneSidedLike.save()
        return Response(oneSidedLike.data, status=status.HTTP_201_CREATED)

api_view(['PUT'])
def MyAPIOne(request):

    data = request.data
    loggedInUserID=data['person1']
    rightSwipedUserID=data['person2']
    rightSwipedAlreadyExists = MatchMake.objects.filter(person1=rightSwipedUserID).exists()
    leftSwipedAlreadyExists = MatchMake.objects.filter(person2=loggedInUserID).exists()

    rightSwipedAlreadyExists2 = MatchMake.objects.filter(person2=rightSwipedUserID).exists()
    leftSwipedAlreadyExists2 = MatchMake.objects.filter(person1=loggedInUserID).exists()
     
    if (rightSwipedAlreadyExists and leftSwipedAlreadyExists) or (rightSwipedAlreadyExists2 and leftSwipedAlreadyExists2):
        # call another api for GET
        api_call = requests.get(updateMatchMake(request), headers={})
        print(api_call.json())

        # call another api for POST
    else:
        data = {} # post data
        api_call = requests.get(newMatchRecord(request), headers={}, data=data)
        print(api_call.json())

    return Response({})


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