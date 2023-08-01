from django.shortcuts import render, HttpResponse

# Create your views here.def blog(request):
def blog(request):
    return HttpResponse("Hello World!")

def index(request):
    return HttpResponse("Hello World!")