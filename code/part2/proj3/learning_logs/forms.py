## 
## forms.py
## ianpasm(kno30826@gmail.com)
## 2018-02-20 09:52:49
## 
 
#!/usr/bin/env python3
# coding=utf-8

from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
