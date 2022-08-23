import requests
import pandas as pd
response = requests.get('https://raw.githubusercontent.com/amylio/Movies-ETL/main/wikipedia-movies.json')
 
print(response)
data=response.json() 
df= pd.DataFrame(data)
print(df.columns)
print(len(data))
print(data[0])