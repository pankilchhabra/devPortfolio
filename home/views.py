from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my homepage(/)")

def about(request):
    return HttpResponse("This is my about page(/about)")

def projects(request):
    return HttpResponse("This is my projects page(/projects)")

def contact(request):
    return HttpResponse("This is my contact page(/contact)")