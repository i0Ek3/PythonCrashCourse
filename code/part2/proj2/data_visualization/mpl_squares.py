## 
## mpl_squares.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-17 15:20:15
## 
 
#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares,linewidth=5)

# set chart title
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# set scaleplate size
plt.tick_params(axis='both',labelsize=14)


plt.show()
