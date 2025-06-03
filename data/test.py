import pandas as pd

file_path = "raw_traffic_data.csv"
df = pd.read_csv(file_path, delimiter=",", encoding="utf-8")
print(df.head())  # Check if data is loaded properly
