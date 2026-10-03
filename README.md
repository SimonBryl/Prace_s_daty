# Pr-ce_s_daty_Br-l
5)
Jako pátý úkol jsem si vybral za cíl zjistit celkové prodeje pro 15 nejznámějších platforem a průměrné prodaje na jednu hru pro každou platformu a zobrazit je v grafu.
- Stejně jako ve všech .py souborech je na 6 až 8 rádku napsaný kód co nejdříve najde relativní cestu do složky přidá k cestě daný csv soubor a v posledním řádku se přes pandas načte celý csv soubor.
- V další fázi kódu si data teprve připravuji. Pomocí metody groupyby dokážu spojit řádky se stejným daným atributem. Já jsem spojil podle platforem. Dál jsem pro dané platformy data sečetl pomocí .sum(), seřadil od největší po nejmenší výsledek a vybral pouze prvních 15 .head(15). Pro průměrné celkové prodeje jsem postupoval stejně až na metoda sum, kterou jsem nahradil metodou mean() pro průměr.
- V poslední fázi už jen stačí dané data zobrazit v grafu. Jelikož jsem chtěl oba grafy ukázat vedle sebe, udělal jsem plátno fig pro dva grafy subplots (1, 2) - jeden řádek a dva sloupce. Pak už jenom daným ax přidělit data a popsat osy. ax[0] jsou průměrný prodeje a ax[1] jsou celkové.

6)
Pro 6 úkol jsem vymyslel zjistit a spočítat pro 5 nejznáméjších vydavatelů celkové prodeje v každém roce a najít rok s maximem a minimem.
- Data jsem si nahrál a groupnul podle vydavatelů. Následně jsem zjistil 5 vydavatelů s největšími celkovými prodeji a jejich číslo indexu si zapamatoval pomocí index.to_list(), abych pak od všech dat vyfiltroval daných 5 vydavatelů pomocí metody .isin()
-  Pak vyfiltrovaný data groupnul na vydavatele společně s rokem a sečetl pro ně celkové prodej. Jelikož  jsem groupoval pomocí dvojce je potřeba resetovat indexy.
-  Teď už stačilo najít daný řádek, kde má daný vydavatel největší a nejmenší prodeje. Pro tento případ kdy si potřebujeme zapamatovat celý řádek použijeme .loc[]. Pak už jen dané data sloučíme pomocí .merge() a přidáme suffixes, kvůli stejným názvům sloupců.

7)
V 7 úkolu jsem chtěl udělat graf vývoje prodejů společnosti Nintendo v jednotlivých letech.
- Data jsem opět načetl vyfiltroval pouze na společnost Nintendo, groupnul je na jednotlivé roky a sečetl pro daný roky celkové prodeje. 
- Dané data jsem pak zobrazil v grafu pomocé .plot() a zvolil si typ 'line'. Popsal jsem osy a nechal zobrazit pomocí mat.show 
