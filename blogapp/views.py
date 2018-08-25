from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from blogapp.blog_page import getblog_bypage
from blogapp.models import *
from blogapp.templatetags.comment_tree import *


# 首页
def index(request):
    article_list = Article.objects.all()
    page = getblog_bypage(article_list, 1)
    return render(request, 'index.html', locals())


# 通过种类获取文章
def category_article(request, cid):
    article_list = Article.objects.filter(category_id=cid)  # 根据种类获取对应的文章
    page = getblog_bypage(article_list, 1)
    return render(request, 'index.html', locals())  # local()函数返回局部变量，包括cid形参


# 点击上一页，下一页获取对应文章
def article_page(request):
    page_number = int(request.GET.get('page', 1))  # 获取传递的页码参数
    cid = request.GET.get('cid')  # 接收种类cid参数
    if cid:  # 如果存在cid,则说明是某个‘种类’进行分页
        article_list = Article.objects.filter(category_id=cid)  # 获取种类对应的文章
    else:  # 没有传递cid，则说明是‘首页’进行分页
        article_list = Article.objects.all()

    page = getblog_bypage(article_list, page_number)
    return render(request, 'index.html', locals())


def getarticle_byid(request):
    aid = request.GET.get('id')
    article = Article.objects.get(id=aid)
    comments = article.comment_set.all()  # 获取文章的所有评论
    print('该文章的所有评论是：', comments)
    # comment_tree = create_comment_tree(comments)  # 创建评论树
    # print('最终的评论树是：', comment_tree)
    return render(request, 'article.html', locals())


def reg(request):
    if request.method == 'GET':
        return render(request, 'reg.html')
    else:
        regname = request.POST.get('regname')
        regpwd = request.POST.get('regpwd')
        regemail = request.POST.get('regemail')
        regtel = request.POST.get('regtel')
        MyUser.objects.create_user(username=regname, password=regpwd, email=regemail, tel=regtel)
        return HttpResponseRedirect(reverse('blogapp:gologin'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        logname = request.POST['username']
        logpwd = request.POST['password']
        user = authenticate(username=logname, password=logpwd)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('blogapp:main'))
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误, 请重新登录！'})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('blogapp:main'))


def addcomment(req):
    user = req.POST.get('user')
    article = req.POST['article']
    content = req.POST['content']
    comment = req.POST['comment']
    username = MyUser.objects.get(username=user)
    if comment == 'none':
        parent = None
    else:
        parent = Comment.objects.get(content=content)

