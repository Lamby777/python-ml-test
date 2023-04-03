import pandas as pd

DATA_FILE_PATH = './melb_data.csv'

data = pd.read_csv(DATA_FILE_PATH) 
out = data.describe()

print(out)
