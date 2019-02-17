from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import Register, LoginForom
from .models import UserModule
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home(request):
    print(request.myuser)
    username = request.session.get('username', '未登录')
    return render(request, 'ss_form/home.html',
                  context={'username': username})


def login_test(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            request.session['username'] = username
            request.session.set_expiry(0) # 关闭浏览器就过期
            return redirect(reverse('ss_home'))
        return HttpResponse('请输入用户名')
    else:
        return render(request, 'ss_form/login.html')

def logout_t(request):
    # request.session.flush()
    logout(request)
    return redirect(reverse('ss_home'))



def register(request):
    if request.method == 'GET':
        form = Register()
        return render(request, 'ss_form/register.html',
                      context={'form': form})
    elif request.method == 'POST':
        form = Register(request.POST) # 里面包含了提交的数据信息
        if form.is_valid(): # 如果提交的数据合法（符合forms设置的规则）
            username = form.cleaned_data['username']
            password = form.cleaned_data.get('password') # get方法不会报错
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password == password_repeat:
                # password = make_password(password) # 在数据库中加密密码
                # UserModule.objects.create(username=username,
                #                           password=password,
                #                           email=email)
                User.objects.create_user(username=username, password=password, email=email)
                return redirect(reverse('ss_login_t'))
            else:
                return HttpResponse('注册失败')
        else:
            error = form.errors
            print(form.errors)
            return HttpResponse(error)

def login_t(request):
    if request.method == 'GET':
        form = LoginForom()
        return render(request, 'ss_form/login_t.html',
                      context={'form': form})
    elif request.method == 'POST':
        form = LoginForom(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # user = UserModule.objects.filter(username=username)
            # # print(user) # <QuerySet [<UserModule: UserModule<username=, password=, email=>>]>
            # 验证用户auth_user表的信息
            user = authenticate(username=username, password=password)
            if user:
                # if check_password(password.user[0].password):
                #     request.session['username'] = username
                #     return redirect(reverse('ss_home'))
                # else:
                #     return render(request, 'ss_form/login_t.html',
                #                   context={'form': form})
                # 实现登陆
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)

                return redirect(reverse('ss_home'))
            else:
                return redirect(reverse('ss_register'))


def permission(request):
    pywjh = User.objects.filter(username='pywjh').first()
    # # 用户表修改密码
    # # pywjh.set_password('123456')
    # # 查权限
    add_blog_permission = Permission.objects.filter(codename='add_blogmodel').first()
    # 给用户添加权限
    pywjh.user_permissions.add(add_blog_permission)


    # 组操作
    # 创建一个组
    # Group.objects.create(name='add_blog_group')
    # 给组添加权限
    # 找到这个新建的组
    g1 = Group.objects.filter(name='add_blog_group').first()
    # g1.permissions.add(add_blog_permission)
    # 找到组员
    Group1 = User.objects.get(username='Group1')
    # 赋予权限
    g1.user_set.add(Group1)

    return HttpResponse('ok')








