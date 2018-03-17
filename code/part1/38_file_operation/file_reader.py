## 
## file_reader.py
## ianpasm(kno30826@gmail.com)
## 2017-11-22 14:29:14
## 
 
#!/usr/bin/env python3
# coding=utf-8

# open current file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# open special file
file_path = '/home/ianpasm/vimrc-diao'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# read one by one
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# create a list which include every line of file contents 
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# use file contents
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))






















