import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

columns = ['datetime','buy_price','sell_price']
data = pd.read_csv("price.csv", delimiter=',', header=None, names=columns)
data['datetime'] = [datetime.fromtimestamp(x) for x in data['datetime']]
x_col  = 'datetime'
y_cols = ['buy_price', 'sell_price']

plt.plot(data[x_col], data[y_cols])
plt.savefig('graph.png')