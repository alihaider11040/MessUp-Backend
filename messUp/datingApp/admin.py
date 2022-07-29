from django.contrib import admin
from .models import Institute, Profile, Country, Profession, SexualOrientation, Zodiac,Interests,MatchMake,Login
# Register your models here.

admin.site.register(Profile)
admin.site.register(SexualOrientation)
admin.site.register(Country)
admin.site.register(Profession)
admin.site.register(Institute)
admin.site.register(Zodiac)
admin.site.register(Interests)
admin.site.register(MatchMake)
admin.site.register(Login)

