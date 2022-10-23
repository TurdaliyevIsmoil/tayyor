from django.contrib import admin
from .models import Category,Company,Job,Majbur,Contact,Rezyume,Blog,Konik,Testimonials

class RezyumeAdmin(admin.ModelAdmin):
    fields = ['your_name','your_email','phone','message','image','image_tag']
    readonly_fields = ['image_tag']
class MajburTabular(admin.TabularInline):
    model = Majbur
class KonikTabular(admin.TabularInline):
    model = Konik
class JobAdmin(admin.ModelAdmin):
    inlines = [MajburTabular,KonikTabular]
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

admin.site.register(Job,JobAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Rezyume,RezyumeAdmin)
admin.site.register(Blog)
admin.site.register(Majbur)
admin.site.register(Konik)
admin.site.register(Testimonials)
# Register your models here.
