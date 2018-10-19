from django.http import HttpResponseRedirect


# 判断是否登录 如果没有登录就跳到登录页面
def login_required(func):
    def login_fun(request, *args, **kwargs):
        # 判断session中是否有user_id,如果没有则认为该用户没有登录
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            response = HttpResponseRedirect('/account/login/')
            # 把访问的路径存到cookie中, key: next_url
            response.set_cookie('next_url', request.get_full_path())
            return response
    return login_fun

"""
http://localhost:8000/account/info/?user=1
request.path:该属性表示当前的路径,返回的是/account/info/
request.get_full_path:表示完整的路径
"""

