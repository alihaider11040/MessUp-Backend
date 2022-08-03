from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from datingApp.serializers import ProfileSerializer, RegisterMatch, Userbymobileserializer, BlockProfile
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute
from datingApp.models import MatchMake, BlockProfile
from messUp.datingApp.serializers import BlockProfileSerializer



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
            return Response(obj, status=status.HTTP_201_CREATED)

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
            return Response(obj, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getUser(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many= False)
    return Response(serializer.data)

def SwipeRight(request):
    data = request.data()
    loggedInUserID=data['loggedInUserID']
    #loggedInUserID=request.loggedInUserID
    rightSwipedUserID=data['rightSwipedUserID']
    #rightSwippedUserID=request.rightSwippedUserID
    rightSwipedAlreadyExists = MatchMake.objects.filter(person1=rightSwipedUserID).exists()
    leftSwipedAlreadyExists = MatchMake.objects.filter(person2=loggedInUserID).exists()
    if rightSwipedAlreadyExists and leftSwipedAlreadyExists:
        match = MatchMake.objects.get(person1= rightSwipedUserID, person2 = loggedInUserID)
        match.person1 = loggedInUserID
        match.person2 = rightSwipedUserID
        match.match_check = True
        match.save()
        content = {'detail': 'Its a match'}        
        matchMade = RegisterMatch(match, many=False)
        return Response(matchMade.data, content)
    else:
        match = MatchMake.objects.create(
            person1=data['loggedInUserID'],
            #person1=request.loggedInUserID,
            person2=data['rightSwipedUserID'],
            #person2=request.rightSwippedUserID,
            match_check=False,
        )
        match.save()
        oneSidedLike = RegisterMatch(match, many=False)
        return Response(oneSidedLike.data, status=HTTP_201_CREATED)


@api_view(['POST'])
def SwipeDown(request):
    data=request.data()
    loggedInUserID=data['loggedInUserID']
    DownSwippedUserID=data['downSwippedUserID']

    DownSwippedAlreadyExists = MatchMake.objects.filter(user1=DownSwippedUserID).exists()
    loggedInAlreadyExists = MatchMake.objects.filter(user2=loggedInUserID).exists()


    DownSwippedAlreadyExists2 = MatchMake.objects.filter(user2=DownSwippedUserID).exists()
    loggedInAlreadyExists2 = MatchMake.objects.filter(user1=loggedInUserID).exists()
    
    if (DownSwippedAlreadyExists and loggedInAlreadyExists) or (DownSwippedAlreadyExists2 and loggedInAlreadyExists2):
        content = {'message': 'Already Blocked'}
        return Response(content)
    else:
        block = BlockProfile.objects.create(
            user1=data['loggedInUserID'],
            #person1=request.loggedInUserID,
            user2=data['rightSwippedUserID'],
            #person2=request.rightSwippedUserID,
            block_check=True,
        )
        block.save()
        BlockProfileMade = BlockProfileSerializer(block, many=False)
        return Response(BlockProfileMade, status=HTTP_201_CREATED)