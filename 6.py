#Cíl: Pro 5 nejznáméjších vydavatelů spočítat celkové prodeje v každém roce a najít rok s maximem a minimem.
import pandas as pan
import numpy as nump
import matplotlib.pyplot as mat
import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "vgsales.csv")
data = pan.read_csv(file_path)

groupedData = data.groupby('Publisher')
bestPublishers = groupedData['Global_Sales'].sum().sort_values(ascending=False).head(5).index.to_list()
filtredPublishers = data[data['Publisher'].isin(bestPublishers)]
salesByYear = filtredPublishers.groupby(['Publisher','Year'])['Global_Sales'].sum()
dataframeSales = salesByYear.reset_index()

best_years = dataframeSales.loc[dataframeSales.groupby('Publisher')['Global_Sales'].idxmax()]
worst_years = dataframeSales.loc[dataframeSales.groupby('Publisher')['Global_Sales'].idxmin()]
mergedData = pan.merge(best_years, worst_years, on='Publisher', suffixes=('_max','_min'))
print (mergedData)
