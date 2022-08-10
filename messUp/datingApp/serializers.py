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
        fields='__all__'
        


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "name",
            "Email_Address",
            "zipcode",
            "Date_of_Birth",
            "password",

        ]

        extra_kwargs = {"password": {"write_only": True}}
        #password = self.validated_data["password"]
        # account.set_password(password)
        # account.save()
        # return account


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profession
        fields=[
        'profession_name'
        ]


class AddProfessionSerializer(serializers.Serializer):
    profession_name=serializers.CharField(max_length=200)
    def create(self,validated_data):
        return Profession.objects.create(**validated_data)



class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institute
        fields=[
        'institution_name'
        ]


class AddInstituteSerializer(serializers.Serializer):
    institution_name=serializers.CharField(max_length=200)
    def create(self,validated_data):
        return Institute.objects.create(**validated_data)




class SexualOrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model=SexualOrientation
        fields=[
            'choice'
        ]



class AddSexualOrientationSerializer(serializers.Serializer):   
    choice=serializers.CharField(max_length=50)
    def create(self,validated_data):
        return SexualOrientation.objects.create(**validated_data)



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=[
            'country_name'
        ]
    def create(self,validated_data):
        return Country.objects.create(**validated_data)


class AddCountrySerializer(serializers.Serializer):
    country_name=serializers.CharField(max_length=200)
    def create(self,validated_data):
        return Country.objects.create(**validated_data)


class ZodiacSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zodiac
        fields=[
            'zodiac'
        ] 


class AddZodiacSerializer(serializers.Serializer):
    zodiac = serializers.CharField(max_length=100)
    def create(self,validated_data):
        return Zodiac.objects.create(**validated_data)




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

class AddLoginSerializer(serializers.Serializer):
    class Meta:
        model=Login
        fields=['phone_number','token','email']

    def create(self,validated_data):
        return Login.objects.create(**validated_data)

class ADDLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    token = serializers.CharField(max_length=100)
    email= serializers.EmailField(max_length=200)
    def create(self,validated_data):
        return Login.objects.create(**validated_data)





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


class AddProfileSerializer(serializers.Serializer):
    class Meta:
        model=Profile
        fields=[
       'username',
       'first_name', 
       'last_name', 
       'city', 
       'bio' ,
       'login',
       'sexualOrientation',
       'country',
       'profession',
       'institute',
       'age',
       'date_of_birth',
       'zodiac',
       'gender'
        ]
    def create(self,validated_data):
            return Profile.objects.create(**validated_data)


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
#copied from Ayila's BRANCH
class filterUsersSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Profile # model used = Profile
        fields=[   # attributes required from Profile model is.
            '__all__'
        ] 