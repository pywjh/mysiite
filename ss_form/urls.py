# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 16:31
# @Author  : wjh
# @File    : urls.py
from django.urls import path
from . import views

urlpatterns =[
    path('login_test/', views.login_test, name='ss_login'), # session登陆
    path('logout_view/', views.logout_t, name='ss_logout_t'), # session退出
    path('home/', views.home, name='ss_home'), # 设置首页，展示用户页
    path('register/', views.register, name='ss_register'), # 注册表单
    path('login_view/', views.login_t, name='ss_login_t'), # 登陆
    path('permission/', views.permission, name='ss_permission'), # 权限设置
]