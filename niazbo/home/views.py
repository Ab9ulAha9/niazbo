from django.shortcuts import render
from .models import home_pics

def home(request):
    pics=home_pics.objects.all()
    return render(request,'home.html' , {'pics':pics , 'total':pics.count()}) 


