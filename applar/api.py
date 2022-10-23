from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from .models import Category,Job
from django.core import serializers
from django.contrib.auth import logout

def api_register(request):
    data=json.loads(request.body)
    username=data['data']
    print(username)
    try:
        user=User.objects.get(username=username)
        user=True
    except:
        user=None
    
    return JsonResponse({'response':user})

def job_category(request,slug,matn):
    b=[]
    if matn=='all':
        if slug=='all':
            jobs=Job.objects.all()
            for job in jobs:
                d = {'name':job.name,'added_date':job.added_date,'company':{'place':job.company.place},'job_type':job.job_type,'jbtype':job.jbtype,'maosh':job.maosh,'category':{'slug':job.category.slug},'pk':job.pk}
                b.append(d)

        else:
            try:
                jobscat=Category.objects.get(slug=slug)
                jobs=jobscat.jobs.all()
                for job in jobs:
                    d = {'name':job.name,'added_date':job.added_date,'company':{'place':job.company.place},'job_type':job.job_type,'jbtype':job.jbtype,'maosh':job.maosh,'category':{'slug':job.category.slug},'pk':job.pk}
                    b.append(d)
            except:
                pass
    else:
        if slug=='all':
            jobs=Job.objects.all().filter(jbtype=matn)
            for job in jobs:
                d = {'name':job.name,'added_date':job.added_date,'company':{'place':job.company.place},'job_type':job.job_type,'jbtype':job.jbtype,'maosh':job.maosh,'category':{'slug':job.category.slug},'pk':job.pk}
                b.append(d)

        else:
            try:
                jobscat=Category.objects.get(slug=slug)
                jobs=jobscat.jobs.all().filter(jbtype=matn)
                for job in jobs:
                    d = {'name':job.name,'added_date':job.added_date,'company':{'place':job.company.place},'job_type':job.job_type,'jbtype':job.jbtype,'maosh':job.maosh,'category':{'slug':job.category.slug},'pk':job.pk}
                    b.append(d)
            except:
                pass
    return JsonResponse(b,safe=False)


def logout_user(request):
    logout(request)
    return JsonResponse({'success':'success'})
