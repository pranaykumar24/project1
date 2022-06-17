from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def haiall(request):
    return HttpResponse('hiall from app11 views')
