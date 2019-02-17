# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 16:08
# @Author  : wjh
# @File    : views.py
from django.http import HttpResponse

def Hello_Django(request):
    return HttpResponse('Hello Django!')