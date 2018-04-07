## 
## setUp.py
## ianpasm(kno30826@gmail.com)
## 2017-11-26 10:13:25
## 
 
#!/usr/bin/env python3
# coding=utf-8

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test AnonymousSurvey class"""
    
    def setUp(self):
        """create an object and a group answers used for test method"""
        question = "What language did you to learn first?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Chinese']

    def test_1(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_3(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()
