#!/usr/bin/env python
# encoding: utf-8
'''
@file: search_indexes.py
@time: 2018/10/12 10:28
'''
from haystack import indexes
from goods.models import GoodsModel


# 这个文件是设置haystack在生成索引时,根据哪些字段来生成索引
class GoodsModelIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)
    def get_model(self):
        return GoodsModel
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

























 