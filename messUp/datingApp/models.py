from audioop import maxpp
import datetime
from distutils.command.upload import upload
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid

class SexualOrientation(models.Model):
    choice = models.CharField(max_length=50, blank=False, null = False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)

    def __str__(self):
        return self.choice


class Country(models.Model):
    country_name = models.CharField(max_length=200, blank=False, null = False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    def __str__(self):
        return str(self.country_name)

class Profession(models.Model):
    profession_name = models.CharField(max_length=200, blank=False, null = False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
   
    def __str__(self):
        return str(self.profession_name)

class Institute(models.Model):
    institution_name = models.CharField(max_length=200, blank=False, null = False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    def __str__(self):
        return str(self.institution_name)

class Zodiac(models.Model):
    ZODIAC_CHOICES=(
        ('Capricon','Capricon'),
        ('Aquarius','Aquarius'),
        ('Pisces','Pisces'),
        ('Aries','Aries'),
        ('Taurus','Taurus'),
        ('Gemini','Gemini'),
        ('Cancer','Cancer'),
        ('Leo','Leo'),
        ('Virgo','Virgo'),
        ('Libra','Libra'),
        ('Scorpio','Scorpio'),
        ('Sagittarius','Sagittarius'),
    )
    zodiac =  models.CharField(max_length=100, choices=ZODIAC_CHOICES)
  
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    def __str__(self):
        return str(self.zodiac)

class Login(models.Model):
    phone_number = models.CharField(max_length=11, null = True, blank=True)
    #passw = models.ForeignKey(Profile, blank=True, null= True,on_delete=models.CASCADE, related_name="+")
    token = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    email= models.EmailField(max_length=200, blank = True, null = True)
    
    def __str__(self):
        return str(self.email)

class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    username= models.CharField(max_length=200, blank=True, null = True)
    first_name = models.CharField(max_length=200, blank=True, null = True)
    last_name = models.CharField(max_length=200, blank=True, null = True)
    city = models.CharField(max_length=200, blank = False, null = False)
    bio = models.TextField(blank = True, null= True)
    gender = models.CharField(max_length=200, choices= GENDER_CHOICES, null=True, blank=True)
    created = models.DateTimeField(auto_now_add= True)
    login = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    sexualOrientation = models.ForeignKey(SexualOrientation,on_delete=models.CASCADE,null=True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True)
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE,null=True)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE,null=True)
    age = models.IntegerField(default= 18)
    d = datetime.date(1997, 10, 19)
    date_of_birth = models.DateField(default = d)
    zodiac = models.ForeignKey(Zodiac, on_delete=models.CASCADE, null=True)
    longitude = models.FloatField(default = 0.0, blank= True, null=True)
    latitude = models.FloatField(default = 0.0, blank= True, null=True)
    def __str__(self):
        return str(self.username)

class PictureGallery(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    profile_image = models.ImageField(null=False, blank = False, upload_to='profiles/', default = "user-default.png")
    image1 = models.ImageField(null=False,blank=False, upload_to='profiles/', default = "user-default.png")
    image2 = models.ImageField(null=True,blank=True, upload_to='profiles/', default = "user-default.png")
    image3 = models.ImageField(null=True,blank=True, upload_to='profiles/', default = "user-default.png")
    image4 = models.ImageField(null=True,blank=True, upload_to='profiles/', default = "user-default.png")
    image5 = models.ImageField(null=True,blank=True, upload_to='profiles/', default = "user-default.png")

    def __str__(self):
        return str(self.user.username)

class Interests(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interestsChoice = models.CharField(max_length=100, blank=False, null = False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)

    def __str__(self):
        return str(self.interestsChoice)


class MatchMake(models.Model):
    person1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="+")
    person2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="+")
    match_check=models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    
    def __str__(self):
        return str(self.match_check)

class BlockProfile(models.Model):
    user1 = models.ForeignKey(Profile, blank= True, null=True,on_delete=models.CASCADE, related_name="+")
    user2 = models.ForeignKey(Profile, blank=True, null= True,on_delete=models.CASCADE, related_name="+")
    block_check=models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)

    def __str__(self):
        return str(self.user1.username + " "+ self.user2.username)

class Notifications(models.Model):
    user = models.ForeignKey(Profile,  blank= True, null=True,on_delete=models.CASCADE),
    notification_message = models.CharField(max_length=500, null=False, blank=False)
    created = models.DateTimeField(auto_now_add= True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)

    def __str__(self):
        return str(self.notification_message)