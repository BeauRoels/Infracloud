rack_struc = {
 "rack": [
      { "Server": { "serv_id": "D1" , 
                    "serv_name": "R1" , 
                    "role": "router"  ,      
                    "services": [   
          {"service": "ad" , "port": "389", "version": "2"},
          {"service": "ntp" , "port": "123", "version": "2"},
          {"service": "dns" , "port": "53", "version": "2"}} 
                     ]
                 }
      },
      { "Server": { "serv_id": "D1" , 
                    "serv_name": "R1" , 
                    "role": "router"  ,      
                    "services": [   
          {"service": "flask" , "port": "8089", "version": "2"},
          {"service": "https" , "port": "443", "version": "2"},
          {"service": "https" , "port": "443", "version": "2"}} 
                     ]
                 }
      },
      { "Server": { "serv_id": "D1" , 
                    "serv_name": "R1" , 
                    "role": "router"  ,      
                    "services": [   
          {"service": "https" , "port": "443", "version": "2"},
          {"service": "https" , "port": "443", "version": "2"},
          {"service": "https" , "port": "443", "version": "2"}} 
                     ]
                 }
      }
   ]
}

        !pip install dicttoxml
from dicttoxml import dicttoxml
xml_data = dicttoxml(rack_struc)
print(xml_data)

print('-----all device interfaces-----')
for device in rack_struc["rack"]:
    print(device["device"]["dev_name"])
    for ipaddress in device["device"]["interfaces"]:
        print(ipaddress["interface"]+" => "+ipaddress["ipaddress"])



        