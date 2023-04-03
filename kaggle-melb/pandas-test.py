import pandas as pd

DATA_FILE_PATH = './melb_data.csv'

features = [
    "Rooms",
    "Bathroom",
    "Landsize",
    "Lattitude",
    "Longtitude", # [sic.]
]

data = pd.read_csv(DATA_FILE_PATH).dropna(axis=0)
x = data[features]
y = data.Price

print(x.head())
