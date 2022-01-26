#curl -i -k -X "OPTIONS" "https://$IP_HOST:443/restconf/data/Cisco-IOS-XE-ntive:native/logging/monitor/severity" \
#-H 'Accept: application/yang-data+json' \
#-u $USERNAME : $PASSWORD

import json
import requests
import datetime
requests.packages.urllib3.disable_warnings()

print("======================================================")
print(datetime.datetime.now())

IP = '192.168.56.101'
api_url = f"https://{IP}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
username = 'cisco'
password = 'cisco123!'
basicauth = (username, password)


resp = requests.options(api_url, auth=basicauth, headers=headers, verify=False)
print("======================================================")
print(resp.raw.version, resp.raw.status, resp.raw.reason)
print("======================================================")
for key, value in resp.headers.items():
    print(f"{key}:{value}")

print("======================================================")