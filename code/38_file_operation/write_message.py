## 
## write_message.py
## ianpasm(kno30826@gmail.com)
## 2017-11-22 14:45:47
## 
 
#!/usr/bin/env python3
# coding=utf-8


# write--if there exist write.txt 'w' will be clear write.txt contents
#      --if not it will be create write.txt
filename = 'write.txt'
with open(filename,'w') as file_object:
    file_object.write("I love python.\n")
    file_object.write("I love you.\n")

# append
filename = 'write.txt'
with open(filename,'a') as file_object:
    file_object.write("Do you like python?\n")

