from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate():
    x=10
    y=32
    return x
def say_hello(request):
    x=calculate()
    return render(request,"hello.html",{"name":"kushal"})