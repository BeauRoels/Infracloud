import requests
import json
current_access_token = "ZDE4ZDg2NmQtMDUxYi00OGE3LWIzYTgtMmRkMWE4YWRkNmYxOWE0ZTVlMTYtNDI3_P0A1_5998ff09-9c27-4407-818f-2305709e8d49"
uri_scheme = 'https://'
uri_authority_server = 'webexapis.com'
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