import sys
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = int(sys.argv[1])  
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print ('arguments:', sys.argv)

month = int(sys.argv[1])

print (f'Hello Mirko for month {month}')