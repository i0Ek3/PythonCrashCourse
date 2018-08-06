## 
## words_count.py
## ianpasm(kno30826@gmail.com)
## 2017-11-22 15:13:42
## 
 
#!/usr/bin/env python3
# coding=utf-8

def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        #msg = "The file " + filename + " does not found!"
        #print(msg)
        pass # no notify whatever
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alicxe.txt'
filename = 'alice.txt'
count_words(filename)
