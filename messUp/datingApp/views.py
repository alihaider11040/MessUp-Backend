import email
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from . import models , serializers, MatchMake



@api_view(['POST'])
def addwithphone(request): #send phone number and OTP i.e token generated for authecation
    #data = request.data()
    phoneNumber=request.GET('phoneNumber')
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
