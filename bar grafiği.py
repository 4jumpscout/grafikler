import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure
import numpy as np
kral=pd.read_json("goals.json")
i=0
j=0
mac_basina_gol=[]
while i<10:
    mac_basina_gol.append((kral[j:j+1]["GOL"])/kral[j:j+1]["MAÇ SAYISI"])
    i=i+1
    j=j+1

figure(figsize=(10,8), dpi=70)
kral["MAÇ BAŞINA GOL"]=mac_basina_gol
plt.axes([0.05,0.05,0.9,0.9])
plt.bar(kral["OYUNCU"],kral["GOL"])
plt.xlabel("OYUNCU")
plt.ylabel("TOPLAM GOL SAYISI")
plt.axes([0.60,0.55,0.3,0.3], facecolor='y')
plt.bar(kral["OYUNCU"],kral["MAÇ BAŞINA GOL"].astype(float))
plt.xlabel("OYUNCU")
plt.ylabel("MAÇ BAŞINA ATILAN GOL SAYISI")

plt.show()