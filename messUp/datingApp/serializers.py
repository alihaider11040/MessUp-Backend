from rest_framework import serializers
from datingApp.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

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
