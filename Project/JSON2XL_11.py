import pandas as pd
import json

with open('/home/ikwildood/Desktop/github/Infracloud/Project/DATAFILE_11.json') as json_file:
    data = json.load(json_file)
df = pd.DataFrame(data)
df.to_excel('/home/ikwildood/Desktop/github/Infracloud/Project/DATAFILE.xlsx')


#df_json = pd.read_json('/home/ikwildood/Desktop/github/Infracloud/Project/DATAFILE_11.json')
#df_json.to_excel('/home/ikwildood/Desktop/github/Infracloud/Project/DATAFILE.xlsx')