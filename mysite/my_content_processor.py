# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 21:54
# @Author  : wjh
# @File    : my_content_processor.py

def my_user(request):
    username = request.session.get('username', '未登录')
    if username:
        return {'myuser': username}
