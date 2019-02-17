# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 20:21
# @Author  : wjh
# @File    : urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('set_ck/', views.set_ck), # 设置cookie
    path('get_ck/', views.get_ck), # 获取cookie
    path('delete_ck/', views.delete_ck) # 删除cookie
]