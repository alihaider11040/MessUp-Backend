from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser,UserImage
from rest_framework.validators import UniqueValidator


class Userbymobileserializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=[
            '__all__'
            ]