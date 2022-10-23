from .models import *
def category(request):
    category = Category.objects.all()
    return {'categories':category}