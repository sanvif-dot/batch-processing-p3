import pandas as pd
from sqlalchemy import create_engine
import os

# assign directory
directory = '/home/sunbee/batchpro/source'
for files in os.listdir(directory):
    
    file_path = os.path.join(directory,files)
    file_name = os.path.basename(file_path).split(".")[0]
    
    if os.path.isfile(file_path):
       print(file_name)
       df = pd.read_csv(file_path, sep =',') 
       engine = create_engine('postgresql://postgres:1997@localhost:5432/postgres')
       df.to_sql(file_name,engine)