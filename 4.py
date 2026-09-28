import pandas as pan
import numpy as nump
import matplotlib.pyplot as mat
import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "vgsales.csv")
data = pan.read_csv(file_path)

filteredData = data[(data.Genre=='Sports')]
filteredData['diff'] = filteredData['NA_Sales']-filteredData['EU_Sales']
filteredData['normDiff'] = (filteredData['NA_Sales']-filteredData['EU_Sales'])/filteredData['Global_Sales']

#statiscké údaje bez normalizace
smOdchylka = round(filteredData['diff'].std(),2)
prumer = round(filteredData['diff'].mean(),2)
median = round(filteredData['diff'].median(),2)
min = round(filteredData['diff'].min(),2)
minIndex = filteredData['diff'].idxmin()
max = round(filteredData['diff'].max(),2)
maxIndex= filteredData['diff'].idxmax()
print("Základní statistické údaje o rozdílu prodejů:","\n-Prodeje běžně kolísají v pásmu (Směrodatnká odchylka): +-",smOdchylka,"\n-O kolik se průměrně se prodalo v NA vůči EU: ", prumer, "\n-Jaký je medián rozdílů v prodeji: ",median)
print("V Evropě se s největším rozdílem oproti Americe prodávala hra ",filteredData.loc[minIndex,'Name']," a to o: ", min*(-1), " milionů")
print("V Americe se s největším rozdílem oproti Evropě prodávala hra ",filteredData.loc[maxIndex,'Name']," a to o: ",max, "miliónů")

#statiscké údaje s normalizací
smOdchylka = round(filteredData['normDiff'].std(),2)
prumer = round(filteredData['normDiff'].mean(),2)
median = round(filteredData['normDiff'].median(),2)
min = round(filteredData['normDiff'].min(),2)
minIndex = filteredData['normDiff'].idxmin()
max = round(filteredData['normDiff'].max(),2)
maxIndex= filteredData['normDiff'].idxmax()
print("Základní statistické údaje o normalizovaném rozdílu prodejů:")
print("- Směrodatná odchylka: +-", smOdchylka)
print("- Průměrný poměrný rozdíl NA vs EU:", prumer)
print("- Medián poměrného rozdílu:", median)
print(f"Hra s největší dominancí v EU: {filteredData.loc[minIndex, 'Name']} (poměrný rozdíl: {min})")
print(f"Hra s největší dominancí v NA: {filteredData.loc[maxIndex, 'Name']} (poměrný rozdíl: {max})")