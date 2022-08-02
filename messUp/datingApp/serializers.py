# HERE import from the rest framework
from rest_framework import serializers

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..datingApp.serializers import ProfileSerializer
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute