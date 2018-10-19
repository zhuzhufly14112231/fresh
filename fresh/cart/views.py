from django.shortcuts import render,redirect
from django.http import JsonResponse

from user.utils import login_required
from cart.models import CartModel
from commen.commen import cart_count_goods
# Create your views here.


@login_required
def cart(request):
    '''购物车'''
    user_id=request.session['user_id']
    carts = CartModel.objects.filter(user_id=user_id)

    return render(request,'cart/cart.html',{'carts':carts})

@login_required
def add(request,goods_id,count):
    '''添加到购物车视图,接受2个参数'''
    user_id = request.session['user_id']
    # 查询购物车中是否已经有这个商品在这个人的名下
    # 如果有,数量增加,如果没有,在购物车中新建一个
    carts = CartModel.objects.filter(user_id=user_id,goods_id=goods_id)
    if len(carts) >= 1:
        new_cart = carts[0]
        new_cart.count = new_cart.count + count
    else:
        new_cart= CartModel()
        new_cart.user_id=user_id
        new_cart.goods_id=goods_id
        new_cart.count = count
    new_cart.save()
    # 如果是ajax请求,则返回一个json
    # 否则转向购物车
    if request.is_ajax():
        cart_count = cart_count_goods(request,CartModel)
        return JsonResponse({'cart_count':cart_count})
    return redirect('/cart/')


@login_required
def delete(request,cart_id):
    '''从购物车中删除某个商品'''
    cart = CartModel.objects.get(id=cart_id)
    cart.delete()
    return JsonResponse({'success':1})

@login_required
def update(request,cart_id,count):
    '''更新购物车内商品数量'''
    cart = CartModel.objects.get(id=cart_id)
    cart.count = count
    cart.save()
    return JsonResponse({'success':1})










