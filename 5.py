#Cíl: Zjistit průměrné a celkové prodeje pro 15 nejznámějších platforem na jednu hru pro každou platformu a zobrazit je v grafu.
import pandas as pan
import numpy as nump
import matplotlib.pyplot as mat
import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "vgsales.csv")
data = pan.read_csv(file_path)

groupedData=data.groupby('Platform')
groupedTop15 = groupedData['Global_Sales'].sum().sort_values(ascending=False).head(15)
groupedPrum = groupedData['Global_Sales'].mean().sort_values(ascending=False).head(15)
fig, ax = mat.subplots(1, 2, figsize=(16, 5))

groupedPrum.plot(kind='bar', ax=ax[0], color='skyblue')
ax[0].set_title('Top 15 platforem – Průměrné prodeje')
ax[0].set_ylabel('Průměrné prodeje (mil.)')
ax[0].set_xlabel('Platforma')

groupedTop15.plot(kind='bar', ax=ax[1], color='orange')
ax[1].set_title('Top 15 platforem – Celkové prodeje')
ax[1].set_ylabel('Celkové prodeje (mil.)')
ax[1].set_xlabel('Platforma')
mat.show()