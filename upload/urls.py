# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 16:31
# @Author  : wjh
# @File    : urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('file/', views.upload), # 文件上传
]