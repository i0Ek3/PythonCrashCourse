## 
## language_survey.py
## ianpasm(kno30826@gmail.com)
## 2017-11-26 09:44:40
## 
 
#!/usr/bin/env python3
# coding=utf-8

from survey import AnonymousSurvey

question = "What language did you like?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' to quit.\n")
while True:
    response = input("language:")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank u for you join the survey!")
my_survey.show_results()
