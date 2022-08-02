from rest_framework import serializers
from datingApp.models import Profile


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
        password = self.validated_data["password"]
        # account.set_password(password)
        # account.save()
        # return account



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
 'username','first_name','last_name','city','bio' ,'profile_image','login','sexualOrientation','id','country' ,'profession' ,'institute','age' ,'d','date_of_birth','zodiac', 'fb_id', 'google_id'

        ]