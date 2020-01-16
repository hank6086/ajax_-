from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import testPost, post2, id_ap,megall
from datetime import datetime
from django.contrib.sessions.models import Session
import random, json, time
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.shortcuts import render
# from .form import idname_uid


def homepage(request):
    posts = testPost.objects.all()
    now = datetime.now()
    print(posts)
    post_lists = list()
    for count, posts in enumerate(posts):
        post_lists.append("NO.{}".format(str(count + 1)) + str(posts))
    # return HttpResponse(post_lists)
    print(locals())
    return render(request, 'index.html', locals())


def test(request):
    posts2 = post2.objects.all()
    # print(posts2)
    stname = list()
    number = list()
    time = list()
    for i in range(len(posts2)):
        stname.append(posts2[i].stname)
    for i in range(len(posts2)):
        number.append(posts2[i].number)
    for i in range(len(posts2)):
        time.append(posts2[i].time)
    # print(locals())
    return render(request, 'index.html', locals())


def megwindows(request):
    textall = ""
    megtextall = megall.objects.all()
    users = id_ap.objects.all()
    for i in range(len(megtextall)):
        for j in range(len(users)):
            if(users[j].uid == megtextall[i].user_uid):
                textall = textall + str(users[j].idname)+ ":" + str(megtextall[i].meg_text) +"\n"
    return render(request, 'index.html', locals())


def add(request):
    if request.GET:
        uid_number = str(request.GET.get('uid'))
        megtext = str(request.GET.get('megtext'))
        megall.objects.create(meg_text=megtext,user_uid=uid_number)
        textall = ""
        megtextall = megall.objects.all()
        users = id_ap.objects.all()
    for i in range(len(megtextall)):
            for j in range(len(users)):
                if(users[j].uid == megtextall[i].user_uid):
                    textall = textall + str(users[j].idname)+ ":" + str(megtextall[i].meg_text) +"<br>"
    return HttpResponse(textall)


def id_naid(request):
    if request.GET:
        idname = str(request.GET.get('idname'))
        uid = str(request.GET.get('uid'))
        id_ap.objects.create(idname=idname, uid=uid)
    return render(request, 'metable.html', locals())


# def set_c(request):
#     response = HttpResponse('Set your lucky_number as 8')
#     response.set_cookie('lucky_number',8)
#     return response

# def get_c(request):
#     if 'lucky_number' in request.COOKIES:
#         return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
#     else:
#         return HttpResponse('No cookies.')

# def set_session(request):
#     response = HttpResponse('Session 儲存完畢!')  #建立 HttpResponse 物件 response
#     request.session["test"] = 9999                #建立 Session
#     return response

# def get_session(request,key=None):
#     if "test" in request.session:                   #檢查指定的session是否存在
#         return HttpResponse(request.session["test"])
#     else:
#         return HttpResponse('Session 不存在!')


