from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.core import serializers
import json
from django.core.paginator import Paginator
def about(request):
    return render(request, 'about.html',{'about1':'active'})
def index(request):
    message=None
    if request.method=='POST':
        if 'fullname' in request.POST:
            fullname=request.POST['fullname']
            email=request.POST['email']
            phone=request.POST['phone']
            text=request.POST['text']
            print(fullname,email,phone,text)
            if 'image' in request.FILES:
                file1=request.FILES['image']
                data=Rezyume(your_name=fullname,your_email=email,phone=phone,message=text,image=file1)
                data.save()
                message="success"
        else:
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            usr=User.objects.create_user(username,email,password)
            usr.is_active=True
            usr.save()
            login(request,usr)
            message="ro'yxatdan o'tdi"
            
    joblar =Testimonials.objects.all()
    category = Category.objects.all()
    jobs1 = Job.objects.all()
    job_urgent=Job.objects.filter(jbtype='Urgent')
    blog = Blog.objects.all()
    context={
        'categories': category,
        'jobs':jobs1,
        'jobs1':job_urgent,
        "msg":message,
        'blogs':blog,
        'index':'active',
        'joblar':joblar
    }
    return render(request, 'index.html', context)
def category_detail(request,slug):
    print('salom')
    cat=Category.objects.get(slug=slug)
    jobs=cat.jobs.all()
    context={
        'slug':cat.name,
        'jobs':jobs,
    }
    return render(request,'category_detail.html',context)
def contact(request):
    context = {'contact':'active'}
    if request.method=="POST":
        first_name=request.POST['first_name']
        email=request.POST['email']
        subject=request.POST['subject']
        text=request.POST['message']
        data=Contact(your_name=first_name,your_email=email,subject=subject,message=text)
        data.save()
        context['msg']="Success"
    return render(request, 'contacts.html',context)
def job_detail(request,slug,pk):
    message=None
    if request.method=='POST':
        if 'fullname' in request.POST:
            fullname=request.POST['fullname']
            email=request.POST['email']
            phone=request.POST['phone']
            text=request.POST['text']
            print(fullname,email,phone,text)
            if 'image' in request.FILES:
                file1=request.FILES['image']
                data=Rezyume(your_name=fullname,your_email=email,phone=phone,message=text,image=file1)
                data.save()
                message="success"
        else:
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            usr=User.objects.create_user(username,email,password)
            usr.is_active=True
            usr.save()
            login(request,usr)
            message="ro'yxatdan o'tdi"
    category=Category.objects.get(slug=slug)
    jobs=category.jobs.get(pk=pk)
    context={
        'jobs':jobs,
         "msg":message
    }
    return render(request, 'job detail.html', context=context)
def jobs(request):
    jobs=Company.objects.all()
    jobs=Job.objects.all()
    p = Paginator(Job.objects.all(), 5)
    page = request.GET.get('page')
    jobs = p.get_page(page)
    data=''
    for job in jobs:
        b = "{'name':'%s','added_date':'%s','company':{'place':'%s'},'job_type':'%s','jbtype':'%s','maosh':'%s','category':{'slug':'%s'},'pk':'%s'},"%(job.name,job.added_date,job.company.place,job.job_type,job.jbtype,job.maosh,job.category.slug,job.pk)
        data=data+b
    if request.method == "POST":
        name = request.POST['name']
        jbtype=request.POST['jbtype']
        maosh=request.POST['maosh']
        jobs=Job.objects.filter(name__contains=name, maosh__contains=maosh,jbtype__contains=jbtype)
        
        return render(request, 'jobs.html',{"jobs":jobs,'data':data,'our_job':'active'})
    else:
        return render(request, 'jobs.html',{"jobs":jobs,'data':data,'our_job':'active'})
def register(request):
    return render(request, 'register.html')
def reset(request):
    return render(request, 'reset password.html')
def sign(request):
    context = {}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            elif user.is_active:
                context["msg"]="top"
                return HttpResponseRedirect('/')
            else:
                context["msg"]="xato"
                return HttpResponseRedirect('/signin')
                
    return render(request, 'sign in.html',context)
def testimonials(request):
    joblar = Testimonials.objects.all()
    context = {
       "joblar":joblar        
    }
    return render(request, 'testimonials.html', context)
def xato(request):
    return render(request, '404.html')

