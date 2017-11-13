#!/usr/bin/env python
# coding=utf-8

prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"

active = True #flag
while active:
    msg = input(prompt)

    if msg == 'quit':
        active = False
    else:
        print(msg)

