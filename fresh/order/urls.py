#!/usr/bin/env python
# encoding: utf-8
'''
@file: urls.py
@time: 2018/10/11 14:22
'''
from django.urls import path
from .views import order,add_order

app_name='order'
urlpatterns= [
    path('',order,name='order'),
    path('add_order/',add_order,name='add_order'),
]

 