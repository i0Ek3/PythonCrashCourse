#!/usr/bin/env python
# coding=utf-8
# Let customer to select when to quit!

prompt = "\nWelcome to my world,please help youself enjoy!"
prompt += "\nJust fun!\n"
msg = ""
while msg != 'quit':
    # msg = input(prompt) #python3
    msg = raw_input(prompt) #python2 
    if msg != 'quit': #avoid to print 'quit'
        print(msg)

