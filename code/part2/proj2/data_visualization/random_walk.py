## 
## random_walk.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-19 13:18:11
## 
 
#!/usr/bin/env python3
# coding=utf-8

from random import choice

class RandomWalk():
    """generate a class for random walk"""

    def __init__(self,num_points=5000):
        """initialize the Attribute of random wal"""

        self.num_points = num_points

        # all the random walk begins with (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """calculate all points which random walk include"""

        # random walk all the time until the list get length appoint
        while len(self.x_values) < self.num_points:
            #decide the forward direction and  distance
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # do not walk on the single point
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next point value (x,y)
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
