#!/usr/bin/env python
# coding=utf-8
# 遍历字典

favorite_languages = {
        'A':'Python',
        'B':'C++',
        'C':'C',
        'D':'Scala',
        'E':'Vala',
        'F':'PHP',
        'G':'Java',
        'H':'Perl',
        'I':'Javascript',
        }

print(favorite_languages)
for key,value in favorite_languages.items():
    print(key + "'s favorite language is: " + value + ".")

for name in favorite_languages.keys():
    print(" " + name)

for language in favorite_languages.values():
    print(" " + language)
 
good = ['A','B']
print(good)
for name in favorite_languages.keys():
    print(name)
    if name in good:
        print("Hello, " + name + ",I saw you favorite language is: " + favorite_languages[name] + ".")
