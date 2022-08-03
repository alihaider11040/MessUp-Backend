import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid

class SexualOrientation(models.Model):
    SEXUAL_ORIENTATION_CHOICES = (
    ('straight','STRAIGHT'),
    ('bisexual', 'BISEXUAL'),
    ('gay','GAY'),
    ('lesbian','LESBIAN'),
    ('all','ALL'),
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

    zodiac =  models.CharField(max_length=100, choices=ZODIAC_SIGNS)
  
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    def __str__(self):
        return str(self.zodiac)

class Login(models.Model):
    phone_number = models.CharField(max_length=11, null = True, blank=True)
    #passw = models.ForeignKey(Profile, blank=True, null= True,on_delete=models.CASCADE, related_name="+")
    token = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    email= models.EmailField(max_length=200, blank = True, null = True)
    
    def __str__(self):
        return str(self.email)

class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    username= models.CharField(max_length=200, blank=True, null = True)
    first_name = models.CharField(max_length=200, blank=True, null = True)
    last_name = models.CharField(max_length=200, blank=True, null = True)
    city = models.CharField(max_length=200, blank = False, null = False)
    bio = models.TextField(blank = True, null= True)
    
    created = models.DateTimeField(auto_now_add= True)
    login = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    sexualOrientation = models.ForeignKey(SexualOrientation,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
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
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
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
        return str(self.interestsChoice)


class MatchMake(models.Model):
    person1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="+")
    person2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="+")
    match_check=models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    
    def __str__(self):
        return str(self.match_check)

class BlockProfile(models.Model):
    user1 = models.ForeignKey(Profile, blank= True, null=True,on_delete=models.CASCADE, related_name="+")
    user2 = models.ForeignKey(Profile, blank=True, null= True,on_delete=models.CASCADE, related_name="+")
    block_check=models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)


