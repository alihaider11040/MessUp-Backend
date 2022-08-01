from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)



