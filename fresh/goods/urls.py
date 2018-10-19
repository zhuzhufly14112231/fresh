#!/usr/bin/env python
# encoding: utf-8
'''
@file: urls.py
@time: 2018/10/9 15:56
'''

from django.urls import path
from goods.views import index,list,detail


app_name='goods'
urlpatterns=[
    path('index/',index,name='index'),
    path('list/<int:category_id>/<str:sort>/<int:page_number>/',list,name='list'),
    path('detail/<int:goods_id>/',detail,name='detail'),
]



 