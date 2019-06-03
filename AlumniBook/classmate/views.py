from django.shortcuts import render
from.models import *

# Create your views here.

def IndexView(request):
    return render(request,'classmate/idenx.html')

def kouView(request):
    return render(request,'classmate/kou.html')





