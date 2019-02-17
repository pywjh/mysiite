from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def set_ck(request):
    response = HttpResponse('设置cookie')
    # response.set_cookie("name", "wakaka", expires=datetime(2018,12,12)) # 截止到那一天过期
    # print(datetime(2018,12,12)) # 2018-12-12 00:00:00
    response.set_cookie("ememem", "hello", max_age=(1000))  # 1000秒以后过期
    return response

def get_ck(request):
    print('cookie:', request.COOKIES)
    print('content:', request.content_type)
    print('encoding:', request.encoding)

    return HttpResponse('获取到cookie')

def delete_ck(request):
    response = HttpResponse('删除cookie')
    response.delete_cookie('name')
    return response

