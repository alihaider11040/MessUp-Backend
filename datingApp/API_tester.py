import requests
from .models import 



endpoint ='http://127.0.0.1:8000/api/addwithphone/'

get_response = requests.get(endpoint, params={'phoneNumber': '03354562152', 'token':'AMKHHJUGGG'})


print(get_response)
