from django.urls import path
from . import views
from .api import api_register,job_category,logout_user

urlpatterns=[
    
    path('', views.index, name='home'),
    path('category/<slug:slug>/',views.category_detail,name="category_detail"),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('<slug:slug>/<int:pk>/', views.job_detail, name='job'),
    path('jobs/', views.jobs, name='jobs'),
    path('register/', views.register, name='register'),
    path('reset/', views.reset, name='reset'),
    path('sign_in/', views.sign, name='signin'),
    path('testimonials/', views.testimonials, name='testimonials'),
    
    
    # API
    
    path('api/register/',api_register,name='api_register'),
    path('job_category/<slug:slug>/<slug:matn>/',job_category,name="job_category"),
    path('logout/',logout_user,name="logout"),
    
]