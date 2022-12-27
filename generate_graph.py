import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

data = pd.read_csv("price.csv", delimiter=',', header=None)
#only use last 50 columns
data = data.iloc[-80:]
data[0] = [datetime.fromtimestamp(x + 25200) for x in data[0]]

plt.figure(figsize=(19.2, 10.8))
plt.xticks(rotation=60)
plt.plot(data[0], data[[1,2]])
plt.savefig('graph.png')
