import pandas as pd
import json

excel_data_df = pd.read_excel('/home/ikwildood/Desktop/github/Infracloud/Project/DATAFILE.xlsx', sheet_name='Datafile')

json_str = excel_data_df.to_json()

print('Excel Sheet to JSON:\n', json_str)

