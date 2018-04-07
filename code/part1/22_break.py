#!/usr/bin/env python
# coding=utf-8

prompt = "\nPlease the name of acity you visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + " !")
