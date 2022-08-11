from rest_framework import serializers
from dataclasses import field
from datingApp.models import Country, Interests, SexualOrientation, Zodiac, MatchMake, Login, Profession, Institute, Profile
from rest_framework.validators import UniqueValidator


class Userbymobileserializer(serializers.ModelSerializer):
    class Meta:
        model= Login
        fields=[
            '__all__'
        ]

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

class ProfessionSerializer(serializers.Serializer):
    class Meta:
        model=Profession
        fields=[
        'profession_name'
        ]

class AddProfessionSerializer(serializers.Serializer):
    profession_name=serializers.CharField(max_length=200)
    def create(self,validated_data):
        return Profession.objects.create(**validated_data)

    
    
class InstituteSerializer(serializers.Serializer):
    class Meta:
        model=Institute
        fields=[
        'institution_name'
        ]

class AddInstituteSerializer(serializers.Serializer):
    institution_name=serializers.CharField(max_length=200)
    def create(self,validated_data):
        return Institute.objects.create(**validated_data)

class SexualOrientationSerializer(serializers.Serializer):
    class Meta:
        model=SexualOrientation
        fields=[
            'choice'
        ]

class AddSexualOrientationSerializer(serializers.Serializer):   
    choice=serializers.CharField(max_length=50)
    def create(self,validated_data):
        return SexualOrientation.objects.create(**validated_data)

class CountrySerializer(serializers.Serializer):
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

class ZodiacSerializer(serializers.Serializer):
    class Meta:
        model=Zodiac
        fields=[
            'zodiac'
        ]

class AddZodiacSerializer(serializers.Serializer):
    zodiac = serializers.CharField(max_length=100)
    def create(self,validated_data):
        return Zodiac.objects.create(**validated_data)


class InterestsSerializer(serializers.Serializer):
    class Meta:
        model=Interests
        fields=[
            'profile','interestsChoice'
        ]
class MatchMakeSerializer(serializers.Serializer):
    class Meta:
        model=MatchMake
        fields=[
            'person1','person2'
        ]
class LoginSerializer(serializers.Serializer):
    class Meta:
        model=Login
        fields=[
            'phone_number','password'
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

class LoginbyIDSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    def create(self,validated_data):
        return Login.objects.create(**validated_data)

class ProfileSerializer(serializers.Serializer):
    profession=ProfessionSerializer(many=True)
    institute=InstituteSerializer(many=True)
    sexualOrientation=SexualOrientationSerializer(many=True)
    country=CountrySerializer(many=True)
    login=LoginSerializer(many=True)
    zodiac=ZodiacSerializer(many=True)
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

class UpdateLocationSerializer(serializers.Serializer):
    class Meta:
        model=Profile
        fields=[
        'longitude',
        'latitude'
        ]
    def create(self,validated_data):
            return Profile.objects.create(**validated_data)

class GetCurrentLocationSerializer(serializers.Serializer):
    longitude = serializers.FloatField(default = 0.0)
    latitude = serializers.FloatField(default = 0.0)
    def create(self,validated_data):
        return Profile.objects.create(**validated_data)

