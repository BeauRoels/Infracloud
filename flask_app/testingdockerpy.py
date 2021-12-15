import json
input_file=open('testingdocker.json', 'r')
output_file=open('test.json', 'w')
json_decode=json.load(input_file)
result = []
for item in json_decode:
    dockernewoutput={}
    dockernewoutput['Id']=item.get('Id')
    dockernewoutput['LastTagTime']=item.get('LastTagTime')
    dockernewoutput['Hostname']=item.get('Hostname')
    print(dockernewoutput)
    result.append(dockernewoutput)
    back_json=json.dumps(result)

