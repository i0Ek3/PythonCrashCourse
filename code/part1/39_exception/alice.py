## 
## alice.py
## ianpasm(kno30826@gmail.com)
## 2017-11-22 15:06:38
## 
 
#!/usr/bin/env python3
# coding=utf-8

filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

