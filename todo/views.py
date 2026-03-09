from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    template=loader.get_template('home.html')
    res=template.render()
    return HttpResponse(res)
def signup(request):
    template=loader.get_template('signup.html')
    res=template.render()
    return HttpResponse(res)
def login(request):
    template=loader.get_template('login.html')
    res=template.render()
    return HttpResponse(res)
    

