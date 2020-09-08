from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse('<h1>First View</h1>')

def second_view(request):
    return HttpResponse('<h1>second View</h1>')

def third_view(request):
    return HttpResponse('<h1>third View</h1>')
