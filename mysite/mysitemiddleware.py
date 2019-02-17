# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 21:07
# @Author  : wjh
# @File    : mysitemiddleware.py.py
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyException(MiddlewareMixin):
    def process_exception(self, request, exception):
        # 当试图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
        print('自定义的process_exception')
        return HttpResponse(exception)
'''
    def process_request(self, request):
        # 执行试图之前被调用，在每个请求上调用，返回None或HttpResponse对象
        print('自定义的 process_request')
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        # 调用试图之前被调用，在每个请求上调用，返回None或HttpResponse
        print('自定义的 process_view')
        return None
    def process_template_response(self, request, response):
        # 试图刚好执行完毕被调用，在每个请求上调用，返回实现了render方法的响应对象
        # 如果试图函数中的返回值中有render方法，才会执行process_template_response
        print('自定义的process_template_response')
        return response
    def process_response(self, request, response):
        # 所有响应返回浏览器之前被调用， 在每个请求上调用，返回HttpResponse
        print('自定义的process_response')
        return response
'''




class UserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request到达view之前执行的代码
        username = request.session.get('username', '未登录')
        if username:
            setattr(request, 'myuser', username)
        # response在试图到达用户浏览器之前执行的代码
        print('request部分的代码')
        response = self.get_response(request)
        print('response部分的代码')
        return response









