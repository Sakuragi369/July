#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2017/1/12 15:46
"""
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^index/?$', views.index),
]
