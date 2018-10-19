#!/usr/bin/env python
# encoding: utf-8
'''
@file: commen.py
@time: 2018/10/10 10:50
'''

# 统计购物车内商品的数量


def cart_count_goods(request, CartModel):
    # 从session中拿到user的id
    user_id = request.session.get('user_id', 0)
    cart_list = CartModel.objects.filter(user_id=user_id)
    cart_count = 0
    # 统计出购物车中所有的商品数量
    for cart in cart_list:
        cart_count += cart.count
    return cart_count