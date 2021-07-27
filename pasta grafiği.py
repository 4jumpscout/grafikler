import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
kral=pd.read_json("goals.json")
i=0
j=0
mac_basina_gol=[]
while i<10:
    mac_basina_gol.append((kral[j:j+1]["GOL"])/kral[j:j+1]["MAÇ SAYISI"])
    i=i+1
    j=j+1

ölçek=[]
label=[]
i=0
j=0

plt.title("Gol krallığındaki oyuncuların gol dağılımları")
plt.pie(kral["GOL"],labels=kral["OYUNCU"], autopct='%1.1f%%', explode=(kral["GOL"]==max(kral["GOL"]))*0.2, shadow=True)
plt.show()