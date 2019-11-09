import requests
import json
from xlwt import *

url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
apiKey ='8c0e5202752a9f00b139b7d0f36bd79f75741975'
filename = 'repo.json'

response = requests.get(url,auth=('token ', apiKey))
repoJSON = response.json()
print(response.json)


for i in response:
    print(i)


file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

