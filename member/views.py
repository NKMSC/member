# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from database.models import Activity , Code,Log,Section,User,UserTakePartInActivity
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def hello(request):
    return HttpResponse('hello world')
def home(request):
    return HttpResponse('this is home')
def reg(request):#注册
    reg=get_template('reg.html',)
    regHtml=reg.render(Context())
    return HttpResponse(regHtml)
def login(request):
	login=get_template('login.html')
	loginHtml=login.render(Context())
	return HttpResponse(loginHtml)

def index(request):# 显示详细信息
    index=get_template('index.html')
    user=request.session.get('user')
    #user = {'name': 'Sally', 'depart':'技术部','grade':'大一','college':'软件学园','major':'软件工程','phone':'15224652255','QQ':'7983452798'}
    
    indexHtml=index.render(Context({'user':user}))
    return HttpResponse(indexHtml)
def index_of_others(request,offset):
    
    index=get_template('index_of_others.html')
    user=User.objects.get(name=offset)
    indexHtml=index.render(Context({'user':user}))
    return HttpResponse(indexHtml)
@csrf_exempt
def edit(request):
    edit=get_template('edit.html')
    user=request.session.get('user')
    editHtml=edit.render(Context({'user':user}))
    return HttpResponse(editHtml)
@csrf_exempt
def edit_result(request):
    sex= request.POST['sex']
    sec=request.POST['sec']
    college= request.POST['college']
    major= request.POST['major']
    grade= request.POST['grade']
    phone= request.POST['phone']
    qq= request.POST['qq']
    province= request.POST['province']
    city= request.POST['city']
    area= request.POST['area']
    campus= request.POST['campus']
    wechat= request.POST['wechat']
    love= request.POST['love']
    dormitory= request.POST['dormitory']
    u=request.session.get('user')
    email=u.email
    user=User.objects.get(email=email)
    
    user.sex=sex
    user.college=college
    user.major=major
    user.grade=grade
    user.phone=phone
    user.qq=qq
    user.province=province
    user.city=city
    user.area=area
    user.campus=campus
    user.wechat=wechat
    user.love=love
    user.dormitory=dormitory
    user.sec=Section.objects.get(id=sec)
    user.save()
    request.session['user']=user
    return HttpResponseRedirect("/index")

def depart(request,offset):
	#depart=get_template('depart.html')
	if offset=='all' :
            userlst=User.objects.all()
            paginator = Paginator(userlst, 5)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                contacts = paginator.page(page)
            except (EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            user=request.session.get('user')
            #user.name='南微软'
            #user.depart='技术部'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'user':user,'contacts':contacts}));
            return HttpResponse(departHtml)
        if offset=='pre' or offset=='2':
            userlst=User.objects.filter(sec=2)
            user=request.session.get('user')
            paginator = Paginator(userlst, 5)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                contacts = paginator.page(page)
            except (EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            #user.name='南微软'
            #user.depart='技术部'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':contacts,'user':user}));
            return HttpResponse(departHtml)
        if offset=='tech' or offset=='1':
            userlst=User.objects.filter(sec=1)
            user=request.session.get('user')
            paginator = Paginator(userlst, 5)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                contacts = paginator.page(page)
            except (EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            #user.name='南微软'
            #user.depart='技术部'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':contacts,'user':user}));
            return HttpResponse(departHtml)
        if offset=='ope' or offset=='3':
            userlst=User.objects.filter(sec=3)
            user=request.session.get('user')
            paginator = Paginator(userlst, 5)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                contacts = paginator.page(page)
            except (EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            #user.name='南微软'
            #user.depart='技术部'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':contacts,'user':user}));
            return HttpResponse(departHtml)
        if offset=='adv' or offset=='4':
            userlst=User.objects.filter(sec=4)
            user=request.session.get('user')
            paginator = Paginator(userlst, 5)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                contacts = paginator.page(page)
            except (EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            #user.name='南微软'
            #user.depart='技术部'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':contacts,'user':user}));
            return HttpResponse(departHtml)
	# 查询数百具
	# 封装对象
	#departHtml=depart.render(Context());
	#return HttpResponse(departHtml)

@csrf_exempt
def reg_result(request):
    password =  request.POST['password']
    if password=='':
        return HttpResponse('注册失败！请填写密码')
    email =  request.POST['email']
    if email=='':
        return HttpResponse('注册失败！请填写邮箱')
    realname =  request.POST['realname']
    if realname=='':
        return HttpResponse('注册失败！请填写真实姓名')
    invitecode =  request.POST['invitecode']
    if invitecode=='':
        return HttpResponse('注册失败！请填写邀请码')
    u=User()
    u.email=email
    u.password=hashlib.sha1(password).hexdigest()
    u.name=realname
    u.sec=Section.objects.get(id=1)
    u.save()
    request.session['user']=u
    result=get_template('result.html')
    resultHtml=result.render(Context())
    return HttpResponse(resultHtml)
@csrf_exempt
def login_result(request):
    password =  request.POST['password']
    if password=='':
        return HttpResponse('登陆失败！请填写密码')
    email =  request.POST['email']
    if email=='':
        return HttpResponse('登陆失败！请填写邮箱')
    u=User()
    u.email=email
    u.password=password
    try:
       user=User.objects.get(email=email)
    except User.DoesNotExist:
        return HttpResponse("账户不存在")
    if user.password==hashlib.sha1(u.password).hexdigest():
        result=get_template('login_result.html')
        resultHtml=result.render(Context())
        request.session['user']=user
        return HttpResponse(resultHtml)
    else:
        return HttpResponse("密码错误")
    

def get_paginator(obj,page):
    page_size = 10 #每页显示的数量
    after_range_num = 5
    before_range_num = 6 
    context = {}
    try:
        page = int(page)
        if page <1 :
            page = 1 
    except ValueError:
        page = 1 
    paginator = Paginator(obj,page_size)
    try:
        obj = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        obj = paginator.page(1)
    
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]
    
    context["page_objects"]=obj
    context["page_range"]=page_range
    return context
   
    
