#!/usr/bin/env python
# encoding: utf-8
'''
@file: urls.py
@time: 2018/10/10 15:31
'''

from django.urls import path
from .views import cart,add,delete,update
app_name='cart'
urlpatterns=[
    path('',cart,name='cart'),
    path('add/<int:goods_id>/<int:count>/',add,name='add'),
    path('delete/<int:cart_id>/',delete,name='delete'),
    path('update/<int:cart_id>/<int:count>/',update,name='update'),
]
 