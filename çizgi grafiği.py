import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
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
#ÇİZGİ GRAFİĞİ GOL SAYISI
plt.axes([0.05,0.05,0.9,0.9])
plt.plot(kral["OYUNCU"],kral["GOL"],'r')
plt.xlabel("OYUNCU")
plt.ylabel("TOPLAM GOL SAYISI")

#ÇİZGİ GRAFİĞİ MAÇ BAŞINA GOL SAYISI
plt.axes([0.60,0.55,0.3,0.3], facecolor='y')
plt.plot(kral["OYUNCU"],kral["MAÇ BAŞINA GOL"],'b')
plt.xlabel("OYUNCU")
plt.ylabel("MAÇ BAŞINA ATILAN GOL ORANI")
plt.show()


