# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:57
# @Author  : wjh
# @File    : forms.py
from django import forms

# 可以写前端代码，但功能主要在于后台信息的验证
class Register(forms.Form):
    username = forms.CharField(max_length=10, min_length=2,
                               error_messages={'min_length': '用户名字长少于2',
                                               'max_length': '用户名不得多于10'}
                               )
    password = forms.CharField(max_length=15, min_length=4,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': '请输入密码'}),
                               error_messages={'min_length': '密码长度小于6',
                                               'max_length': '密码长度超过8了'}
                               )
    password_repeat = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

class LoginForom(forms.Form):
    username = forms.CharField(max_length=10, min_length=2,)
    password = forms.CharField(max_length=15, min_length=4,
                               widget=forms.PasswordInput())