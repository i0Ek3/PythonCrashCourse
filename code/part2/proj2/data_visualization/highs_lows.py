## 
## highs_lows.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-22 11:05:43
## 
 
#!/usr/bin/env python3
# coding=utf-8

import csv
from matplotlib import pyplot as plt


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

    #for index,column_header in enumerate(header_row):
    #    print(index,column_header)

# drawing graphic based on data
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')

#set style
plt.title("Daily high tempertures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperture (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()




