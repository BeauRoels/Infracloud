import requests
import json
current_access_token = "valid token"
uri_scheme = 'https://'
uri_authority_server = 'api.ciscopark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + uri_api_path

headers = {
    'Authorization' : 'Bearer {}'.format(current_access_token),
    'Content-Type': 'Application/json'
}
res = requests.get(url, headers=headers)
user_name = res.json()['displayName']

if res.status_code==200:
    print("status ok")
    print("Username: " + user_name)
else:
    print("status not ok")