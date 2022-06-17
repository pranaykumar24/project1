from django.contrib import admin
from django.http import HttpResponse

# Register your models here.
def app22(request):
    return HttpResponse('hello from app22 views')
