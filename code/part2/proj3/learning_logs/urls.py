## 
## urls.py
## ianpasm(kno30826@gmail.com)
## 2017-12-05 17:52:41
## 
 
#!/usr/bin/env python3
# coding=utf-8

"""define learning_logs's URL pattern"""

from django.conf.urls import url

from . import views

urlpatterns = [
        # mainpage
        url(r'^$',views.index,name='index'),
        
        # show all topics
        url(r'^topics/$',views.topics,name='topics'),
        
        # detail page of specific topic
        url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
        ]
