from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def students(request):
    std=student.objects.all()
    return render(request,'studentlist.html',{'std':std})
def contact(request):
    return HttpResponse('<h1>This is Contactpage</h1>')

