#Cíl:Udělat graf vývoje prodejů společnosti Nintendo v jednotlivých letech
import pandas as pan
import numpy as nump
import matplotlib.pyplot as mat
import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "vgsales.csv")
data = pan.read_csv(file_path)

filteredData = data[data.Publisher=='Nintendo']
groupedData = filteredData.groupby('Year')
groupedDatasum = groupedData['Global_Sales'].sum()
groupedDatasum.plot(kind='line', marker='o', figsize=(10, 5), grid=True)
mat.xlabel('Rok')
mat.ylabel('Prodeje (mil. kusů)')
mat.show()