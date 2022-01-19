import requests
import json

iphost = "192.168.56.101"
interface = "GigabitEthernet1"
username = "cisco"
password = "cisco123!"


#Curl in python

headers = {
    'Accept': 'application/yang-data+json',
}

response = requests.get('https://'+ iphost+ '/restconf/data/ietf-interfaces:interfaces/interface=' + interface, headers=headers, verify=False, auth=('$USERNAME', '$PASSWORD'))



if response.status_code==200:
    print("status ok")
   
else:
    print("status not ok")