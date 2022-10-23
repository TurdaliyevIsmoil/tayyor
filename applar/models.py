from operator import mod
from django.db import models
from django.utils.safestring import mark_safe

class Category(models.Model):
	name=models.CharField(max_length=255,unique=True)
	slug=models.SlugField(max_length=255,unique=True)
	code=models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Company(models.Model):
	name=models.CharField(max_length=255)
	place=models.CharField(max_length=255)
	email=models.EmailField(default="example@mail.com")
	phone=models.IntegerField(default=998901234567)
	text = models.TextField()
    
	def __str__(self):
		return self.name


class Job(models.Model):
	JBTYPE=(
		('Intership','Intership'),
		('Part-time','Part-time'),
		('Urgent','Urgent')
	)

	jbtype=models.CharField(max_length=255,choices=JBTYPE)
	category=models.ForeignKey(Category,related_name='jobs',on_delete=models.CASCADE)
	company=models.ForeignKey(Company,related_name='jobs',on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	job_type=models.CharField(max_length=255)
	text=models.TextField()
	majburiyat=models.CharField(max_length=255)
	konikma=models.CharField(max_length=255)
	maosh=models.CharField(max_length=255)
	added_date=models.DateField(auto_now_add=True, null=True)
	def __str__(self):
		return self.name

class Majbur(models.Model):
	jobs=models.ForeignKey(Job,related_name="majburi",on_delete=models.CASCADE)
	majburiyat=models.CharField(max_length=255)

class Konik(models.Model):
	jobs=models.ForeignKey(Job,related_name="konikm",on_delete=models.CASCADE)
	konikma = models.CharField(max_length=255)


class Contact(models.Model):
	your_name = models.CharField(max_length=150)
	your_email = models.EmailField(max_length=150)
	subject = models.CharField(max_length=255)
	message = models.TextField()
	def __str__(self):
		return self.your_name

class Rezyume(models.Model):
	your_name = models.CharField(max_length=150)
	your_email = models.EmailField(max_length=150)
	phone=models.CharField(max_length=100)
	message = models.TextField()
	image=models.ImageField(upload_to='rezyume/%Y/%m/%d/')
	def __str__(self):
		return self.your_name

	def image_tag(self):
		return mark_safe('<img src="http://127.0.0.1:8000/media/%s" width="150" height="150" />' % (self.image))
	image_tag.short_description = 'Image'
class Blog(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    def __str__(self):
	    return self.text
class Testimonials(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    def __str__(self):
	    return self.text
