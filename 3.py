import pandas as pan
import numpy as nump
import matplotlib.pyplot as mat
import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "vgsales.csv")
data = pan.read_csv(file_path)

filtredData = data[(data.Year>=1985)&(data.Year<=2010)]
grouped = filtredData.groupby('Year')
byYearDict= {}
for year, group in grouped:
    cor = group['NA_Sales'].corr(group['EU_Sales'])
    byYearDict[year] = cor

mat.figure(figsize=(12, 8))
mat.scatter(byYearDict.keys(), byYearDict.values())
mat.xlabel('year')
mat.ylabel('correlation')
mat.show()