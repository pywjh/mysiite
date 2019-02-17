from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.
from .models import BlogModel
from django.contrib.auth.decorators import login_required, permission_required

@permission_required('bolg.add_blogmodel')
def add(request):
    if request.method == 'GET':
        return render(request, 'blog/demo_add.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 存入数据库
        bb = BlogModel(title=title, content=content)
        bb.save()
        # BlogModel.objects.get_or_create(title=title, content=content)
        # 重定向到添加页面
        return redirect(reverse('blog_add'))

from django.views import View


class BlogAdd(View):
    def get(self, request):
        return render(request, 'blog/demo_add.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 存入数据库
        bb = BlogModel(title=title, content=content)
        bb.save()
        return redirect(reverse('blog_add'))


# def add_handle(request): # 把action中的路径去掉，表示数据提交到当前网页
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     # 存入数据库
#     BlogModel(title=title, content=content).save()
#     # 重定向到添加页面
#     return redirect(reverse('blog_add'))


@login_required
def index(request):
    return render(request, 'blog/demo_index.html')


def list(request):
    blog_list = BlogModel.objects.all()
    return render(request, 'blog/demo_list.html',
                  context={'blog_list': blog_list})


def detail(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    return render(request, 'blog/demo_detail.html',
                  context={'blog': blog})


def delete(request, blog_id):
    blog = BlogModel.objects.filter(id=blog_id)
    if blog:
        blog.delete()
        return redirect(reverse('blog_list'))
    return HttpResponse('没有此博客!')


def edit(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    if blog:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            blog.title = title
            blog.content = content
            blog.save()
            return redirect(reverse('blog_list'))
        content = blog.content
        return render(request, 'blog/demo_edit.html',
                      context={'blog':blog, 'content': content})
    return HttpResponse('没有此博客!')

#
# def edit_handle(request, blog_id):
#     blog = BlogModel.objects.get(id=blog_id)
#     if blog:
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         blog.title =title
#         blog.content = content
#         blog.save()
#         return redirect(reverse('blog_list'))
#     else:
#         return HttpResponse('没有博客内容!')