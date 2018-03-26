## 
## americas.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-26 11:06:38
## 
 
#!/usr/bin/env python3
# coding=utf-8

import pygal

wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

wm.add('North America',['ca', 'mx', 'us'])
wm.add('Central',['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')



