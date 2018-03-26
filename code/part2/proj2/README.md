# Data Visualization

## Generate Data

### Install [matplotlib](http://matplotlib.org)
```Shell
$ pip install --user matplotlib # for macOS
$ sudo apt install python3-matplotlib # for linux
```
Other way you can visit [this site](http://www.lfd.uci.edu/-gohlke/pythonlibs/#matplotlib) to download matplotlib.<br>

Then you need test your matplotlib follows under codes,if no errors output,that means its work.<br>
```Shell
$ python   # on my macOS I need run python,maybe you should run python3
>>> import matplotlib
>>>
```

### Draw Simple Line Chart

Write your own mpl_squares.py file then run `python mpl_squares.py` to check it.<br>
![15-2](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-2.png)<br>

The chart you can see something wrong,so we need add `input_values` for plot() to revise chart.<br>
![15-2_1](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-2_1.png)<br>

Use scatter() to draw scatter point chart as well as set its style.Then you can see a point on the chart like this.<br>
![15-4](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-4.png)<br>
Now we transfer two parameters to scatter() to draw a series of points.<br>
![15-5](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-5.png)<br>
![15-6](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-6.png)<br>

We need to add a parameter `edgecolor` to scatter() to delete data point outline and add a parameter `c` to set data point color(or use RGB).<br>
![15-6_1](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-6_1.png)<br>

We can use `cmap` parameter to implement color reflect.You can visit [this site](http://matplotlin.org) then click Examples to select Color Examples then click colormaps_reference to check something about color map.<br>
![15-7](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-7.png)<br>

Additional,you can call savefig() to place show() to save figure in your files.<br>

### Wander Random

Create class RandomWalk() which includes method __init__() and fill_walk().<br>

Drawing the random walk chart.<br>
![15-8](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-8.png)<br>

Simulate random walk times more and set its style.<br>
![15-9](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-9.png)<br>

Redrawing origin and destination and hide coordinate.<br>
![15-10](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-10.png)<br>

### Use Pygal simulate dicing

Install Pygal and go to [this site](http://www.pygal.org) to check Pygal gallery.<br>
```Shell
$ pip install --user pygal==1.7
```

Then you should create a Die class and throw dice.<br>

Drawing histogram then you can check .svg file to see chart which holds interaction.<br>
![15-11](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-11.png)<br>

Now we will throw two dices in the same time.<br>
![15-12](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-12.png)<br>

Now we will throw two dices with different sides in the same time.<br>
![15-13](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/15-13.png)<br>


## Download Data

### CSV Type File

CSV file:data value divided by series of comma.Then fetch data and drawing graphic.<br>
![16-1](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/16-1.png)<br>

Use model datatime to add date in wheather file.<br>
![16-2](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/16-2.png)<br>

Create whole years wheather graphic.Then drawing more a series of data.<br>
![16-4](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/16-4.png)<br>

Colour for area.<br>
![16-5](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/16-5.png)<br>

Error checking.<br>
```Shell
$ python highs_lows.py
(datetime.datetime(2014, 2, 16, 0, 0), 'missing data')
```
![16-6](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/16-6.png)<br>

### Making JSON Type World Population Map

Fetch data(two letter nationality code) and convert it into some type which pygal can deal.<br>

Making world map.<br>
![16-7](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/16-7.png)<br>

Show the data on the world map.<br>
![16-8](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj2/pic/16-8.png)<br>



