## 
## survey.py
## ianpasm(kno30826@gmail.com)
## 2017-11-26 09:37:11
## 
 
#!/usr/bin/env python3
# coding=utf-8

class AnonymousSurvey():
    """收集匿名调查的答案"""

    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""

        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self,new_response):
        """存储单份调查问卷答案"""
        
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的答案"""

        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
