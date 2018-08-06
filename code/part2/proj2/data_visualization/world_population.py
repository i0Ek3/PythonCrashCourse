## 
## world_population.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-26 10:45:11
## 
 
#!/usr/bin/env python3
# coding=utf-8

import json
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle 


#load data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# create a dict which includes population
cc_populations = {}
#print all country population on 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# grouping country into three part accroding population
cc_pops_1,cc_pops_2,cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))


wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010,by Country'
#wm.add('2010',cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')



