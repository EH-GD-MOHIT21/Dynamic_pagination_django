from django.shortcuts import render
from django.http import HttpResponse as httpres
from .models import paginationdata as pad
from math import ceil
# Create your views here.

def home(request,pageno=1):
    pageno = int(pageno)
    data_len = len(pad.objects.all())
    data = pad.objects.all()[(pageno-1)*21:pageno*21]
    limit = ceil(data_len/21)
    if pageno > limit:
        return httpres("<h1 style='text-align:center;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:red;'>Required Data Doesnot Exist on Server. </h1>")
    limit = [0 for i in range(limit)]
    return render(request,'index.html',{'data':data,'total':data_len , 'limit':limit , 'page':pageno})