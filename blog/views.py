from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# request要加
def hello_world(request):
    # 要把回傳的東西包裝成HttpResponse物件
    return HttpResponse("Hello world!")