import pandas as pd
import os

data={'Name':['Alice','Bob','Charlie','Shubham','Aditya'],
      'Age':[20,25,30,35,40],
      'City':['NewYork','Charlie','Bob','Patna','Delhi']
      }

df=pd.DataFrame(data)

data_dir="data"
os.makedirs(data_dir,exist_ok=True)

filepath=os.path.join(data_dir,'sample_data.csv')
df.to_csv(filepath,index=False)
print(f"data saved successfully to the path {filepath}")