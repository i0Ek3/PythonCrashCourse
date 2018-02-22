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

        # a page as add a new topic
        url(r'^new_topic/$',views.new_topic, name='new_topic'),

        # a page as add a new topic
        url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),

        # a page as a item edit
        url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),

        ]
