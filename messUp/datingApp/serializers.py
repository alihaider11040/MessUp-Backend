from dataclasses import fields
from difflib import Match
from rest_framework import serializers
from datingApp.models import Profile, Login, MatchMake

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class Userbymobileserializer(serializers.ModelSerializer):
    class Meta:
        model= Login
        fields=[
            '__all__'
        ]

class RegisterMatch(serializers.ModelSerializer):
    class Meta:
        model = MatchMake
        fields=[
            '__all__'
        ]