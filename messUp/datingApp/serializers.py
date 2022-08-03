# HERE import from the rest framework
from rest_framework import serializers
from datingApp.models import Profile, Profession, Zodiac, Login, Interests, SexualOrientation, Institute

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

class getUsersBy_age_and_GenderSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Profile # model used = Profile
        fields=[   # attributes required from Profile model is.
            '__all__'
        ] 