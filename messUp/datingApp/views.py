from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from datingApp.serializers import ProfileSerializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute


@api_view(['GET'])
def getRoutes(request):

    routes = [
        
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getUser(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many= False)
    return Response(serializer.data)



