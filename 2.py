import pandas as pan
import numpy as nump
import matplotlib as mat
import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "vgsales.csv")
data = pan.read_csv(file_path)
print("pearson")
print(data['NA_Sales'].corr(data['EU_Sales'],'pearson')) #Pearson
print("Spearmanův")
print(data['NA_Sales'].corr(data['EU_Sales'],'spearman'))
print("Kendal")
print(data['NA_Sales'].corr(data['EU_Sales'],'kendall'))