## 
## na_populations.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-26 13:58:29
## 
 
#!/usr/bin/env python3
# coding=utf-8

import pygal

wm = pygal.Worldmap()
wm.title = 'Populations of Countries in North America'
wm.add('North America',{'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')

