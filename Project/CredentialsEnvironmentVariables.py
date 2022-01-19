   ### RESTCONF IETF-INTERFACES -- CREDENTIALS ENTERED BY USER
import requests
import urllib3
from decouple import config
# Disable SSL Verification Warning because of Private SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
restconf_router_ip = config('CSR1Kv')  # "192.168.56.107"
restconf_user = config('RESTCONFUSER') # cisco
restconf_psw = config('RESTCONFPASW')  # cisco123!
api_url = "https://{0}/restconf/data/ietf-interfaces:interfaces".format(restconf_router_ip)
print("restconf url: " + api_url)
# fout zal 406 weergeven
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
print(headers)
#verkeerd wachtwoord zou 401 moeten weergeven
basicauth =(restconf_user,restconf_psw)
resp = requests.request('GET', api_url, auth=basicauth, headers=headers, verify=False)
print(resp.text)
if resp.status_code==200:
    print("status ok")
   
else:
    print("status not ok")