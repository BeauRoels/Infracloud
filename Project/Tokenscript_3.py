#### DEVASC LAB 3.6.6
import json
atk = {
 "access_token":"ZZDE4ZDg2NmQtMDUxYi00OGE3LWIzYTgtMmRkMWE4YWRkNmYxOWE0ZTVlMTYtNDI3_P0A1_5998ff09-9c27-4407-818f-2305709e8d49",
 "expires_in":1209600,
 "refresh_token":"ZDE4ZDg2NmQtMDUxYi00OGE3LWIzYTgtMmRkMWE4YWRkNmYxOWE0ZTVlMTYtNDI3_P0A1_5998ff09-9c27-4407-818f-2305709e8d49",
 "refreshtokenexpires_in":7776000
}
print('-----1-----')
print (type(atk))
print('-----1B-----')
print(atk.keys())
print('-----2-----')
#### pretty output
print(json.dumps(atk, indent=8))
#### FILTERING DATA
#### filter access-token
print('-----3-----')
print(atk["access_token"])
#### TRANSFORMING DATA TYPES
print('-----4-----')
ats = json.dumps(atk)  #### SERIALIZATION
print(type(ats))
####
print('-----5-----')
atj = json.loads(ats)
print(type(atj))
