# -*- coding: utf-8 -*-
import random
import hashlib
import smtplib  
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from database.models import Activity , Code,Log,Section,User,UserTakePartInActivity
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from constant_number import * # 引入常量


def hello(request):
    return HttpResponse('hello world')

def home(request):
    return HttpResponse('this is home')

def reg(request):#注册
    try:
        invitecode=request.GET.get('invitecode', '')
    except ValueError: 
        invitecode = ''
    reg=get_template('reg.html',)
    regHtml=reg.render(Context({'invitecode':invitecode}))
    return HttpResponse(regHtml)

def login(request):
    user=request.session.get('user')
    if user is None:
        login=get_template('login.html')
        loginHtml=login.render(Context())
        return HttpResponse(loginHtml)
    else:
        return HttpResponseRedirect("/index")# 跳转到个人主页

def index(request):# 显示自己的详细信息
    index=get_template('index.html')
    user=request.session.get('user')# 从session对象里面拿出user对象，session是运行这个网站时，每个页面
    if user is None: #都共有的一个公共对象，所以可以利用它来在各个页面之间传递参数之类
        return HttpResponse("请先登录！")# 如果session里面没有user对象，说明用户并没有登陆，所以返回错误页面
    #user = {'name': 'Sally', 'depart':'技术部','grade':'大一','college':'软件学园','major':'软件工程','phone':'15224652255','QQ':'7983452798'}
    
    indexHtml=index.render(Context({'user':user}))
    return HttpResponse(indexHtml)

def index_of_others(request,offset):# 显示别人的详细信息
    # offset是其他用户的name
    index=get_template('index_of_others.html')
    user=User.objects.get(id=int(offset))# 从数据库里查找所点击的用户
    u=request.session.get('user')# 没登陆的话报错
    if u is None:
        return HttpResponse("请先登录！")
    indexHtml=index.render(Context({'user':user}))
    return HttpResponse(indexHtml)

@csrf_exempt
def edit(request):
    edit=get_template('edit.html')
    user=request.session.get('user')
    if user is None:
        return HttpResponse("请先登录！")
    editHtml=edit.render(Context({'user':user}))
    return HttpResponse(editHtml)

@csrf_exempt
def edit_result(request):# 编辑页面返回的结果
    sex= request.POST['sex']# 从前台的表单中拿回各种数据
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
    user=User.objects.get(email=email)#数据库里拿到所编辑的对象
    if user is None:
        return HttpResponse("请先登录！")
    
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
    user.dormitory=dormitory# 保存修改
    user.sec=Section.objects.get(id=sec)
    user.save()# 修改后的对象存入数据库
    request.session['user']=user# 用新的user替换掉之前旧的session里面的user对象
    return HttpResponseRedirect("/index")# 跳转到个人主页

def depart(request,offset):
	#depart=get_template('depart.html')
        user=request.session.get('user')
        if user is None:
            return HttpResponse("请先登录！")
	if offset=='all' :# 如果访问的网址是 depart/all的话，返回所有的用户信息
            #userlst=User.objects.all()
            userlst=User.objects.filter(effective = 1)
            paginator = Paginator(userlst, 5) # 分页系统，每页显示5个用户
            try:
                page = int(request.GET.get('page', '1'))# 访问的网址是depart/all/page=?
            except ValueError: # 这里的page对象就是“？”后面的数字，用来标记访问的第几页
                page = 1# 出错的话直接访问第一页
            try:
                contacts = paginator.page(page)
            except (EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            user=request.session.get('user')
            #user.name='南微软'
            #user.depart='技术部'
            isactive='active'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'user':user,'contacts':userlst,'isactive1':isactive}))
            return HttpResponse(departHtml)
        if offset=='pre' or offset=='2':# 如果访问的是depart/pre或者 depart/2，显示主席团的成员信息
            userlst=User.objects.filter(sec=2, effective=1)# 主席团的部门id是2，其他与上面相同
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
            isactive='active'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':userlst,'user':user,'isactive2':isactive}))
            return HttpResponse(departHtml)
        if offset=='tech' or offset=='1':# 技术部
            userlst=User.objects.filter(sec=1, effective=1)
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
            isactive='active'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':userlst,'user':user,'isactive3':isactive}))
            return HttpResponse(departHtml)
        if offset=='ope' or offset=='3': #运营部
            userlst=User.objects.filter(sec=3, effective=1)
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
            isactive='active'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':userlst,'user':user,'isactive4':isactive}))
            return HttpResponse(departHtml)
        if offset=='adv' or offset=='4': #宣传
            userlst=User.objects.filter(sec=4, effective=1)
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
            isactive='active'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':userlst,'user':user,'isactive5':isactive}))
            return HttpResponse(departHtml)
        if offset=='cons' or offset=='6': #顾问
            userlst=User.objects.filter(sec=6,effective=1)
            user=request.session.get('user')
            paginator = Paginator(userlst,5)
            try:
                page = int(request.GET.get('page','1'))
            except ValueError:
                page = 1
            try:
                contacts = paginator.page(page)
            except (EmptyPage,InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            isactive='active'
            depart=get_template('depart.html')
            departHtml=depart.render(Context({'contacts':userlst,'user':user,'isactive7':isactive}))
            return HttpResponse(departHtml)
	# 查询数百具
	# 封装对象
	#departHtml=depart.render(Context());
	#return HttpResponse(departHtml)
	if offset=='me':
            return HttpResponseRedirect("/index")
        if offset=='logout':
            return HttpResponseRedirect("/logout")
        if offset=='edit':
            return HttpResponseRedirect("/edit")
            

@csrf_exempt
def reg_result(request): # 注册的结果页面
    u=User() # 新建一个User对象，把它存入数据库
    password =  request.POST['password'] #从表单里拿到密码
    if password=='': # 没填密码
        return HttpResponse('注册失败！请填写密码')
    email =  request.POST['email']
    if email=='':# 没填邮箱
        return HttpResponse('注册失败！请填写邮箱')
    name =  request.POST['name']
    if name=='':
        return HttpResponse('注册失败！请填写真实姓名')
    invitecode =  request.POST['invitecode']
    if invitecode=='':
        return HttpResponse('注册失败！请填写邀请码')
    sec = request.POST['sec']
    if sec==u'主席团':
        u.sec=Section.objects.get(id=2)
    if sec==u'技术部':
        u.sec=Section.objects.get(id=1)
    if sec==u'运营部':
        u.sec=Section.objects.get(id=3)
    if sec==u'宣传部':
        u.sec=Section.objects.get(id=4)
    if sec==u'顾问团':
        u.sec=Section.objects.get(id=5)
    
    college = request.POST['college']
    major = request.POST['major']
    entry_year = request.POST['entry_year']
    grade = request.POST['grade']
    campus = request.POST['campus']
    sex = request.POST['sex']
    phone = request.POST['phone']
    province = request.POST['province']
    city = request.POST['city']
    area = request.POST['area']
    qq = request.POST['qq']
    love = request.POST['love']
    #city = request.POST['city']

    u.school='南开大学'
    u.email=email
    u.password=hashlib.sha1(password).hexdigest() # 这是生成hash值代替明文的密码
    u.name=name
    u.college=college
    u.major=major
    u.entry_year=entry_year
    u.grade=grade
    u.campus=campus
    u.sex=sex
    u.phone=phone
    u.province=province
    u.city=city
    u.area=area
    u.qq=qq
    u.love=love
    u.effective=1
    u.authority=0

    try: # 测试邮箱是否已经被使用过了
        User.objects.get(email = email)
    except User.DoesNotExist:
        pass
    else:
        return HttpResponse("该邮箱已被注册,请您换一个未被注册过的有效邮箱进行注册!")

    try:
        c=Code.objects.get(code=invitecode)
        if c.effective==0:
            return HttpResponse("该邀请码已经被使用过了！请确认您拥有正确的邀请码！")
        else:
            u.save()
            c.effective=0
            c.use =User.objects.get(email = email)  # 把验证码和用户关联上
            c.save()
    except Code.DoesNotExist:
        return HttpResponse("该邀请码不存在！请确认您拥有正确的邀请码！")
    
    request.session['user']=u # 把user对象放到session里面去
    result=get_template('result.html')
    resultHtml=result.render(Context())
    return HttpResponse(resultHtml)

@csrf_exempt
def login_result(request): # 登陆的结果
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
       user=User.objects.get(email=email) # user是指从数据库里面查找的邮箱为email的用户
    except User.DoesNotExist:
        return HttpResponse("账户不存在")
    if user.password==hashlib.sha1(u.password).hexdigest(): # u是登陆之时填写的用户
        if user.effective == 1:
            result=get_template('login_result.html') # 比较数据库的用户的密码和填写的密码是否一致
            resultHtml=result.render(Context())
            request.session['user']=user
            return HttpResponseRedirect("/index")
        else:
            return HttpResponse("您的帐号已被删除或封停,具体情况请联络技术部负责人予以解决!")
    else:
        return HttpResponse("密码错误")
@csrf_exempt
def change_code(request):  #修改密码
    user = request.session.get('user')
    if user is None :
        return HttpResponse("请先登陆！")
    result = get_template('change_password.html')
    result_html = result.render(Context({'return_value_old':True,'return_value_new':True}))
    return HttpResponse(result_html)

@csrf_exempt
def change_code_result(request):  #修改密码的结果
    u = request.session.get('user')
    old_password = request.POST['old_password']
    old_password = hashlib.sha1(old_password).hexdigest() 
    new_password = request.POST['new_password']
    confirm_password = request.POST['password_confirm']
    if u is None :
        return HttpResponse("请先登陆！")
    result = get_template('change_password.html')
    bad_result_html = result.render(Context({'return_value_old':False,'return_value_new':False}))
    if old_password is None:
        return HttpResponse(bad_result_html)
        #return HttpResponse('1')  # 被注释掉的是调试哪一个部分出错了，觉得没用可以删掉(-__-)
    if new_password is None:
        return HttpResponse(bad_result_html)
        #return HttpResponse('2')
    if confirm_password is None:
        return HttpResponse(bad_result_html)
        #return HttpResponse('3')
    if u.password != old_password:
        if new_password != confirm_password:
            return HttpResponse(bad_result_html)
            #return HttpResponse('4')
        else:
            bad_result_html = result.render(Context({'return_value_old':False,'return_value_new':True}))
            return HttpResponse(bad_result_html)
            #return HttpResponse(u.password)
    if new_password != confirm_password:
        bad_result_html = result.render(Context({'return_value_old':True,'return_value_new':False}))
        return HttpResponse(bad_result_html)
        #return HttpResponse('6')
    user = User.objects.get(email = u.email)
    user.password = hashlib.sha1(new_password).hexdigest()
    user.save()
    request.session['user'] = user
    return HttpResponseRedirect("/index")

@csrf_exempt
def reset_code_request(request):   #在登陆页面点击找回密码
    result = get_template('reset_password.html')
    result_html = result.render(Context({'return_value_email':True}))
    return HttpResponse(result_html)

@csrf_exempt
def reset_code(request):  #发送重置邮件获取验证码
    email = request.POST['email']
    #email="754884172@qq.com"
    try:
        user = User.objects.get(email = email)
        #return HttpResponse(user);
        subject = u'南微软通讯录信息录入通知'
        msg_t = get_template("mail_confirm.html")
        success = 1
        code = ''
        while True:    # 防止号码重复
            code = getstr(8)
            try:
                Code.objects.get(code=code)
            except Code.DoesNotExist:
                break
        if send_mail([email], subject, msg_t.render(Context({'code':code}))):
            c = Code()
            c.code = code
            c.use = User.objects.get(email = email)  
            #old_code = Code.objects.get(user = c.user)
            #old_code.effective = 0
            #old_code.save()
            #c.type = CODE_TYPE['invite'] # CODE_TYPE ？？？#
            c.start_time = datetime.now()
            c.effective = 1
            try:                     #设定有效时间为五分钟，因为进位问题写的很恶心。。望跟进
                c.end_time = c.start_time + timedelta(minutes=5) 
                c.save()
            except :
                c.effective = 0
                c.end_time = c.start_time
                return HttpResponse("时间运算出错啦，请联系系统管理员!")
        else:
            success = 0 
        if success:
            return HttpResponse("邮件发送成功，请您查收！")      
        else:
            return HttpResponse("邮件发送失败，请重试，为我们的失误感到万分抱歉！")
    except User.DoesNotExist:
        bad_result = get_template('reset_password.html')
        bad_result_html = bad_result.render(Context({'return_value_email':False}))
        return HttpResponse(bad_result_html)
    
@csrf_exempt
def reset_code_change(request): #重设密码
    result = get_template('reset_password_2.html')
    result_html = result.render(Context())
    return HttpResponse(result_html)

@csrf_exempt
def reset_code_result(request): #返回重设密码的结果
    password = request.POST['password']
    password_confirm = request.POST['password_confirm']
    code_confirm = request.POST['code']
    bad_result = get_template('reset_password_2.html')
    if password is None:
        bad_result_html = bad_result.render(Context({'return_value_notempty':False}))
        return HttpResponse(bad_result_html)
    if password_confirm != password:
        bad_result_html = bad_result.render(Context({'return_value_notdiff':True}))
    try:
        code=Code.objects.get(code = code_confirm)
        if code.effective==0:   #判定验证码是否有效
            bad_result_html = bad_result.render(Context({'return_value_wrongstr':False}))
            return HttpResponse(bad_result_html)
        time = datetime.now()
        if time > code.end_time:
            code.effective=0
            bad_result_html = bad_result.render(Context({'return_value_wrongstr':False}))
            return HttpResponse(bad_result_html)
        email = code.use.email
        user = User.objects.get(email = email)
        user.password = hashlib.sha1(password).hexdigest()
        code.effective = 0
        user.save()
        request.session['user'] = user
        return HttpResponseRedirect("/login")
    except Code.DoesNotExist: #判定验证码是否存在
        bad_result_html = bad_result.render(Context({'return_value_wrongstr':False}))
        return HttpResponse(bad_result_html)

def get_paginator(obj,page): # 这个函数不用管它
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

def logout(requst):# 注销，从session里面删除user对象，并跳转回登陆页面
    user=requst.session.get('user')
    if user is None:
        return HttpResponse("请先登录！")
    del requst.session['user']
    return HttpResponseRedirect("/login")

def getstr(n):#获得指定长度随机字符串
    st = ''
    while len(st) < n:
        temp = chr(97+random.randint(0,25))
        if st.find(temp) == -1 :
            st = st.join(['',temp])
    return st

def send_mail(to_list,sub,content):  
    mail_host="smtp.qq.com"  #设置服务器
    #mail_user="member@nkumstc.cn"    #用户名
    #mail_pass="password"   #密码

    mail_user="997833949"    #用户名
    mail_pass="renyujie910"   #密码
    mail_postfix="qq.com"
    me="南微软"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='html',_charset='utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False
#mailto_list=["XXX@qq.com"] # 发送对象的列表
# send_mail(mailto_list,"hello","hello world！")

def send_code(request):
    user=request.session.get('user')
    if user is None:
        return HttpResponse("请先登录！")
    elif User.objects.get(id = user.id).authority & AUTHORITY['admin'] == 0: # 这个地方最好以后能改成try形式
        return HttpResponse("您不具有管理员资格！")
    else:
        s_c=get_template('send_code.html',)
        s_cHtml=s_c.render(Context())
        return HttpResponse(s_cHtml)

@csrf_exempt
def send_code_result(request):
    user=request.session.get('user')
    if user is None:
        return HttpResponse("请先登录！")
    elif User.objects.get(id = user.id).authority & AUTHORITY['admin'] == 0: # 这个地方最好以后能改成try形式
        return HttpResponse("您不具有管理员资格！")
    else:
        pass
    email_list_raw = request.POST['email_list']
    subject = u'南微软通讯录信息录入通知'
    msg_t = get_template("mail_invite.html")
    email_list = email_list_raw.split('\n')
    success = 1
    for email_addr in email_list:
        code = ''
        while True:
            code = getstr(8)
            try:
                Code.objects.get(code=code)
            except Code.DoesNotExist:
                break
        if send_mail([email_addr], subject, msg_t.render(Context({'code':code}))):
            c = Code()
            c.code = code
            c.use = User.objects.get(id=0)  # a special user means nobody
            c.type = CODE_TYPE['invite']
            c.start_time = datetime.now()
            c.effective = 1
            c.end_time = datetime.now().replace(year=9999) # forever effective
            c.save()
        else:
            success = 0
            break
    if success:
        return HttpResponse("发送邀请码邮件成功!")
    else:
        return HttpResponse("操作失败!")
 
