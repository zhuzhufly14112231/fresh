from django.urls import path
from user.views import register, register_post, login, info, logout,all_order,upload
# 命名空间
app_name = 'user'
urlpatterns = [
    path('register/', register, name='register'),
    path('register_post/', register_post, name='register_post'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # 用户信息接口
    path('info/', info, name='info'),
    path('all_order/<int:page_num>/',all_order,name='all_order'),
    # 文件上传
    path('upload/',upload,name='upload'),
]