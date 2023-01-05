import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

data = pd.read_csv("price.csv", delimiter=',', header=None)
#only use last 50 columns
data = data.iloc[-80:]
data[0] = [datetime.fromtimestamp(x + 25200) for x in data[0]]
data.columns=['Time', 'Buy price', 'Sell price']
data.plot(kind='line', grid=True, x=0, y=[1,2], xlabel="Time", ylabel="Price(vnd)", figsize=[19.2, 10.8])
plt.savefig('graph.png')
