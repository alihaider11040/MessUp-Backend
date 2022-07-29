from pydoc import describe
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
import uuid

class SexualOrientation(models.Model):
    SEXUAL_ORIENTATION_CHOICES = (
    ('straight','STRAIGHT'),
    ('bisexual', 'BISEXUAL'),
    ('gay','GAY'),
    ('lesbian','LESBIAN'),
    )

    choice = models.CharField(max_length=50, choices=SEXUAL_ORIENTATION_CHOICES)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)

    def __str__(self):
        return self.choice


class Country(models.Model):
    country_name = models.CharField(max_length=200, blank=False, null = False)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    def __str__(self):
        return str(self.country_name)

class Profession(models.Model):
    PROFESSION_CHOICES = (
    ('doctor','Doctor'),
    ('accountant', 'Accountant'),
    ('engineer','Engineer'),
    ('teacher','Teacher'),
    ('manager','Manager'),
    ('business','Business Man'),
    )
    profession_name = models.CharField(max_length=200,  choices=PROFESSION_CHOICES)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
   
    def __str__(self):
        return str(self.profession_name)

class Institute(models.Model):
    INSTITUTE_CHOICES = (
    ('nuces','National University of Computer and Emerging Sciences'),
    ('nust', 'National University of Sciences and Technology'),
    ('giki','Ghulam Ishaq Khan Institute'),
    ('ucp','University of Centeral Punjab'),
    ('gcu','Government College University'),
    ('pu','Punjab University'),
    )
    institution_name = models.CharField(max_length=200,  choices=INSTITUTE_CHOICES)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
   
    def __str__(self):
        return str(self.institution_name)

class Zodiac(models.Model):
    ZODIAC_SIGNS = (
    ('aries','Aries'),
    ('taurus','Taurus'),
    ('gemini','Gemini'),
    ('cancer','Cancer'),
    ('leo','Leo'),
    ('virgo','Virgo'),
    ('libra','Libra'),
    ('scorpio','Scorpio'),
    ('sagittarius','Sagittarius'),
    ('capricon','Capricon'),
    ('aquarius','Aquarius'),
    ('pisces','Pisces'),
    )

    zodiac = models.OneToOneField('Profile', blank=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    username= models.CharField(max_length=200, blank=True, null = True)
    first_name = models.CharField(max_length=200, blank=True, null = True)
    last_name = models.CharField(max_length=200, blank=True, null = True)
    email= models.EmailField(max_length=200, blank = True, null = True)
    city = models.CharField(max_length=200, blank = False, null = False)
    bio = models.TextField(blank = True, null= True)
    profile_image = models.ImageField(null=True, blank = True, upload_to='profiles/', default = 'profiles/user-default.png')
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    sexualOrientation = models.ForeignKey(SexualOrientation,on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null = True, blank=True)    
    
    def __str__(self):
        return str(self.user.username)

class Interests(models.Model):
    INTEREST_CHOICES = (
    ('selfcare','Self-Care'),
    ('yoga', 'Yoga'),
    ('writing','writing'),
    ('meditaion','Meditation'),
    ('sushi','Sushi'),
    ('hockey','Hockey'),
    ('basketball','Basketball'),
    ('poetry','Slam Poetry'),
    ('hworkouts','Home Workouts'),
    ('manga','Manga'),
    ('makeup','Make-up'),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interestsChoice = models.CharField(max_length=100, choices=INTEREST_CHOICES)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)

    def __str__(self):
        return self.interestsChoice


class MatchMake(models.Model):
    person1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="+")
    person2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="+")

    match_check=models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)

class Login(models.Model):
    phone_num = models.ForeignKey(Profile, blank= True, null=True,on_delete=models.CASCADE, related_name="+")
    passw = models.ForeignKey(Profile, blank=True, null= True,on_delete=models.CASCADE, related_name="+")
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)