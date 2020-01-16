from django.shortcuts import render
from django.http import HttpResponse
# from .models import Post
from datetime import datetime
# Create your views here.

def homepage(request):
    now = datetime.now()
    return render(request,'index.html',locals())

