from django.test import TestCase

# Create your tests here.
# @api_view(['PUT'])
# def user_update_view(request):    
#     data = request.data    
#     fbid=data['fbId']    
#     alreadyExists = CustomUser.objects.filter(fbId=fbid).exists()    
#     if alreadyExists:        
#         user = CustomUser.objects.get(fbId=fbid)        
#         user.firstName = data['firstName']        
#         user.lastName = data['lastName']        
#         user.gender = data['gender']        
#         user.age = data['age']        
#         user.jobTitle = data['jobTitle']        
#         user.location = data['location']            
#         user.school = data['school']        
#         user.save()        
#         Customuser = CustomUserSerializer(user, many=False)    
#     else:        
#         content = {'detail': 'user not exist'}        
#         return Response(content)    
#     return Response(Customuser.data)