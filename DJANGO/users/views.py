from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse('123456')

# Create your views here.
def index(request):# request请求返回对象
    return HttpResponse('123123')