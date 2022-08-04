from rest_framework import serializers
from . import models
from rest_framework.validators import UniqueValidator
from dataclasses import field
from .models import Login, Profile, Institute, Profession, Interests, SexualOrientation
from .models import Country, Zodiac, MatchMake, BlockProfile

#testmyfetch

class Userbymobileserializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields=[
            '__all__'
        ]

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profession
        fields=[
        'profession_name'
        ]
class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institute
        fields=[
        'institution_name'
        ]
class SexualOrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model=SexualOrientation
        fields=[
            'choice'
        ]

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=[
            'country_name'
        ]

class ZodiacSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zodiac
        fields=[
            'zodiac'
        ] 
class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interests
        fields=[
            'profile','interestsChoice'
        ]
class MatchMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=MatchMake
        fields=[
            'person1','person2','match_check'
        ]
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=[
            'phone_number','token','email'
        ]

class ProfileSerializer(serializers.ModelSerializer):
    profession=ProfessionSerializer(many=False)
    institute=InstituteSerializer(many=False)
    sexualOrientation=SexualOrientationSerializer(many=False)
    country=CountrySerializer(many=False)
    login=LoginSerializer(many=False)
    zodiac=ZodiacSerializer(many=False)

    class Meta:
        model=Profile
        fields=[
 'username','first_name','last_name','city','bio','gender','login','sexualOrientation','country' ,'profession' ,'institute','age','date_of_birth','zodiac'

        ]


class RegisterMatch(serializers.ModelSerializer):
    class Meta:
        model = MatchMake
        fields=[
            'person1','person2','match_check'
        ]

class BlockProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockProfile
        fields=[
            'user1', 'user2','block_check'
        ]
