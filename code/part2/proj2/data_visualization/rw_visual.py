## 
## rw_visual.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-19 13:35:36
## 
 
#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# when process activate then simulate random walk times more
while True:
    #create instance for RandomWalk and draw the all point its includes
    rw = RandomWalk(50000)
    rw.fill_walk()

    # set drawing windows size
    plt.figure(dpi=128,figsize=(10,6))

    plt.scatter(rw.x_values,rw.y_values,s=15)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)
    
    #extrude origin and destination
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    
    # hide coordinate
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    
    plt.show()

    # pay attention for the function input() usage in different version,maybe you should use raw_input()
    keep_running = raw_input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
