## 
## urls.py
## ianpasm(kno30826@gmail.com)
## 2018-02-22 20:13:10
## 
 
#!/usr/bin/env python3
# coding=utf-8

"""define URL pattern for application users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # login page
    url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),

    # logout page
    url(r'^logout/$',views.logout_view, name='logout'),

    # register page
    url(r'^register/$', views.register, name='register'),
]
