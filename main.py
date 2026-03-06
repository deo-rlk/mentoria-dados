import requests
import pandas as pd

url = 'https://raw.githubusercontent.com/Moscarde/Junior_Zone/automation/data/googlesheets_dataset.csv'

data = pd.read_csv(url, sep=',')
dataFrame = pd.DataFrame(data)

path = 'C:/Users/odewaldo.rodrigues_i/Desktop/GitHub/mentoria-dados/dados/vagas/data.json'

output = dataFrame.to_json(orient='index',indent=1 ,date_format='iso', path_or_buf=path)


#data.to_json(storage_options='C:/Users/odewaldo.rodrigues_i/Desktop/GitHub/mentoria-dados/dados/vagas')

print(output)