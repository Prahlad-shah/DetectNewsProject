from django.shortcuts import render
from requests import request
from django.http import HttpResponse
from ml.news_detection import predict
import tensorflow as tf

def index(request,*args,**kwargs):
    if request.method == 'POST':
        info = request.POST['news']
        result,predi = predict(info)    
        return render(request,'index.html',{'val':predi,'res':result})
    return render(request,'index.html')

def homePageView(request):
    return render(request, 'home.html')

# Create your views here.   
