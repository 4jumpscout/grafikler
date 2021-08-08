import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
kral=pd.read_json("goals.json")
ölçek=[]
label=[]

plt.title("Gol krallığındaki oyuncuların gol dağılımları")
plt.pie(kral["GOL"],labels=kral["OYUNCU"], autopct='%1.1f%%', explode=(kral["GOL"]==max(kral["GOL"]))*0.2, shadow=True)
plt.show()
