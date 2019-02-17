# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 16:19
# @Author  : wjh
# @File    : urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='blog_index'),
    path('add/', views.add, name='blog_add'),
    path('blog_add/', views.BlogAdd.as_view()),
    # path('add_handle', views.add_handle, name='blog_add_handle'),
    path('list/', views.list, name='blog_list'),
    path('detail/<blog_id>/', views.detail, name='blog_detail'),
    path('delete/<blog_id>/', views.delete, name='blog_delete'),
    path('edit/<blog_id>/', views.edit, name='blog_edit'),
    # path('edit_handle/<blog_id>/', views.edit_handle, name='blog_edit_handle')
]