import requests
from requests.models import Response
import json

with open('./url.json') as json_file:
    json_data = json.load(json_file)
for k in json_data.keys():
    print(k + ': ', json_data[k])
for k in json_data.keys():
    Response = requests.get(json_data[k])
    if Response.status_code == 200:
        print(json_data[k]+':Success!')
    elif Response.status_code != 200:
        print(json_data[k]+':Test Failed!!Error Code:'+ str(Response.status_code))