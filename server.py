import json
rack_struc = {
 "rack": [
      { "Server": { "serv_id": "D1" , 
                    "serv_name": "R1" , 
                    "role": "router"  ,      
                    "services": [   
          {"service": "https" , "port": "443", "version": "2"},
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
import yaml
yaml_data = yaml.dump(rack_struc)
print(yaml_data)

print('-----all device interfaces-----')
for device in rack_struc["rack"]:
    print(device["device"]["dev_name"])
    for ipaddress in device["device"]["interfaces"]:
        print(ipaddress["interface"]+" => "+ipaddress["ipaddress"])