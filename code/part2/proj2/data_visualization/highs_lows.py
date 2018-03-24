## 
## highs_lows.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-22 11:05:43
## 
 
#!/usr/bin/env python3
# coding=utf-8

import csv
from matplotlib import pyplot as plt
from datetime import datetime

#fetch date and the highest temperature from file
#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else: 
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    #print(highs)

    #for index,column_header in enumerate(header_row):
    #    print(index,column_header)

# drawing graphic based on data
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#set style
title = "Daily high and low tempertures - 2014\nDeath Valley,CA"
plt.title(title,fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperture (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()




