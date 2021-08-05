from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Create your views here.
def index(request):

   
    return render(request,'index.html')
def click(request):
    return render(request,'click.html')
def show(request):
    return render(request,'show.html')  
def info(request):
    return render(request,'info.html') 