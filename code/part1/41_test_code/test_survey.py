## 
## test_survey.py
## ianpasm(kno30826@gmail.com)
## 2017-11-26 09:52:49
## 
 
#!/usr/bin/env python3
# coding=utf-8

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test AnonymousSurvey class"""
    

    def test_store_single_response(self):
        question = "What language did you to learn first?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English',my_survey.responses)

    def test_3(self):
        question = "What language did you to learn first?"
        my_survey = AnonymousSurvey(question)
        responses = ['Mexcio','English','French']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)


unittest.main()
