from datingApp.models import Country, Interests, SexualOrientation, Zodiac, MatchMake, Login, Profession, Institute, VerifyCode, Profile
from rest_framework import serializers

class ProfessionSerializer(serializers.Serializer):
    class Meta:
        model=Profession
        fields=[
        'profession_name'
        ]
class InstituteSerializer(serializers.Serializer):
    class Meta:
        model=Institute
        fields=[
        'institution_name', 'id'
        ]
class SexualOrientationSerializer(serializers.Serializer):
    class Meta:
        model=SexualOrientation
        fields=[
            'choice',
            'id'
        ]

class CountrySerializer(serializers.Serializer):
    class Meta:
        model=Country
        fields=[
            'country_name','id'
        ]

class ZodiacSerializer(serializers.Serializers):
    class Meta:
        model=Zodiac
        fields=[
            'zodiac','id'
        ] 
class InterestsSerializer(serializers.Serializers):
    class Meta:
        model=Interests
        fields=[
            'profile','interestsChoice','id'
        ]
class MatchMakeSerializer(serializers.Serializers):
    class Meta:
        model=MatchMake
        fields=[
            'person1','person2','id'
        ]
class LoginSerializer(serializers.Serializers):
    class Meta:
        model=Login
        fields=[
            'phone_number','password','id'
        ]

class ProfileSerializer(serializers.Serializers):
    profession=ProfessionSerializer(many=True)
    institute=InstituteSerializer(many=True)
    sexualOrientation=SexualOrientationSerializer(many=True)
    country=CountrySerializer(many=True)
    login=LoginSerializer(many=True)
    zodiac=ZodiacSerializer(many=True)
    class Meta:
        model=Profile
        fields=[
 'username','first_name','last_name','city','bio' ,'profile_image','login','sexualOrientation','id','country' ,'profession' ,'institute','age' ,'d','date_of_birth','zodiac'

        ]
#class VerifyCodeSerializer(serializers.Serializers):
    #class Meta:
        #model=VerifyCode
       # fields=[
           # 'mobile','email','code','add_time'
       # ]