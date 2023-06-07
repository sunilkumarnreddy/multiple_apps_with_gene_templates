from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_htmlpage(request):
    return render(request,'app1_htmlpage.html')

def app1_string(request):
    return HttpResponse('<center><h1 style >This is app1_string Response,Hello fellows! ..</h1></center>')


