import pandas as pan
import numpy as nump
import matplotlib.pyplot as mat
import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "vgsales.csv")
data = pan.read_csv(file_path)
filteredData = data[(data.Year>=1990)&(data.Year<2000)]
valueCaunts = filteredData.Genre.value_counts()
valueCaunts.plot(kind='bar')
mat.show()
