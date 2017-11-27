#!/usr/bin/env python
# coding=utf-8

#1
def greet(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['maya','jimio','lio','andy']
greet(usernames)


#2 modified the list in function
unprint_designs = ['piglet','flowers','biupol']
completed_models = []

while unprint_designs:
    current_design = unprint_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


#3 reconstrcutor #2
def print_models(unprint_designs,completed_modelsl):
    while unprint_designs:
        current_design = unprint_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design) 

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprint_designs = ['piglet','flowers','biupol']
completed_models = []

print_models(unprint_designs,completed_models)
show_completed_models(completed_models)


#4 banned to modified function list
# you can use 
#   function_name(list_name[:])来传递副本
# [:]切片表示法用来创建列表的副本
