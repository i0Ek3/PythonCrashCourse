# Data Visualization


## Install [matplotlib](http://matplotlib.org)
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

## Draw Simple Line Chart

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
