#!/usr/bin/env python
# coding=utf-8

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
print("\n")
#print(aliens)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['speed'] = 'fast'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print("\n")

#修改外星人的属性
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['speed'] = 'fast'
        alien['points'] = 10
    elif alien['color'] == 'blue':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'slow'
    else:
        print("No more color aliens to be modified!")

for alien in aliens[:5]:
    print(alien)
print("...")
print("\n")
