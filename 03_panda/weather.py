# if you grt any error in this code, then you need to install pandas library using pip install pandas command in your terminal.
import pandas as pd

df = pd.read_csv('dataset.csv')

# temaparue maximum and minimum
print("Maximum Temperature:", df['Temperature'].max())
print("Minimum Temperature:", df['Temperature'].min())

# get me rains days
rain_days = df[df['Events'] == 'Rain']
print("Rainy Days:")
print(rain_days)