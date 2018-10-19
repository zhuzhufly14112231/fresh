from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import CategoryModel, CategoryGoodsModel,GoodsModel
from cart.models import CartModel
from commen.commen import cart_count_goods

# Create your views here.



def index(request):
    """主页"""

    # 拿出所有的分类
    category_list = CategoryModel.objects.all()

    # 分别取出分类下的最新的商品
    new_goods_dict = {} # 存储每个分类下的最新的商品
    for category in category_list:
        # 直接通过商品分类id从goods中获取当前分类的商品
        goods_list = GoodsModel.objects.filter(category_id=category.id).order_by('-id')[:4]
        new_goods_dict[category] = goods_list
    cart_count=cart_count_goods(request,CartModel)

    context = {
        'new_goods_dict': new_goods_dict,
        'cart_count': cart_count,
    }
    return render(request, 'goods/index.html', context)


def list(request,category_id,sort,page_number):

    '''商品列表视图
    category_id:分类的id
    page_number:获取当前页的页码
    sort:排序字段(默认:default,价格:price,人气:popularity)'''

    category=CategoryModel.objects.get(id=category_id)
    # 取该类型最新的两个商品
    news=GoodsModel.objects.filter(category_id=category_id).order_by('-id')[:2]
    # 外键的用法
    # news=category.goodsmodel_set.order_by('-id')[:2]

    if sort == 'default':  #默认排序
        goods_list=GoodsModel.objects.filter(category_id=category_id).order_by('-id')
    elif sort=='price':
        goods_list=GoodsModel.objects.filter(category_id=category_id).order_by('-price')
    else:
        goods_list=GoodsModel.objects.filter(category_id=category_id).order_by('-popularity')
    # 根据商品的列表goods_list进行分页
    paginator = Paginator(goods_list,2)
    page = paginator.page(page_number)
    cart_count=cart_count_goods(request,CartModel)
    context={
        'category':category,  # 商品的分类对象
        'news':news, # 新品推荐
        'goods_list':goods_list, # 排序后的商品列表
        'sort':sort, # 排序的条件
        'cart_count':cart_count,  #购物车的商品数量
        'page':page,
        'page_num':page_number
    }
    return render(request,'goods/list.html',context)

def detail(request,goods_id):
    """某个商品的详细信息"""
    goods=GoodsModel.objects.get(id=goods_id)
    goods.popularity += 1  #增加商品的人气值
    goods.save()
    # 利用orm外键的特性
    news=goods.category.goodsmodel_set.order_by('-id')[:2]
    cart_count=cart_count_goods(request,CartModel)

    # 记录最近的浏览记录,在用户中心使用
    # 判断是否已经登录
    if request.session.has_key('user_id'):
        user_id=str(request.session.get('user_id'))
        goods_list=request.session.get(user_id,[])
        if not goods_list: # 判断是否有浏览记录
            goods_list.append(goods.id)
        else:
            # 如果已经存在浏览的商品,删除掉这一个
            if goods_id in goods_list:
                goods_list.remove(goods_id)
            goods_list.insert(0,goods_id)  # 添加元素到列表的第一个
            # 如果超过5个浏览记录,删除最后一个
            if len(goods_list) > 5:
                del goods_list[-1]
        # 最近浏览的商品存储在session中,以user_id的值为key
        request.session[user_id]=goods_list
    return render(request,'goods/detail.html',{'goods':goods,'news':news,'cart_count':cart_count})

