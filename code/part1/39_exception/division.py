## 
## division.py
## ianpasm(kno30826@gmail.com)
## 2017-11-22 14:56:19
## 
 
#!/usr/bin/env python3
# coding=utf-8


# you need python3 to run it
# deal ZeroDivisionError 
try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide by zero!")

# instance 2
print("Give me 2 numbers,and I'll calculate they divide.Enter 'q' to end." )

while True:
    num1 = input("\nFirst number: ")
    if num1 == 'q':
        break
    num2 = input("\nSecond number: ")
    try:
        answer = int(num1) / int(num2)
    except ZeroDivisionError:
        print("You cant do this!")
    else:
        print(answer)






