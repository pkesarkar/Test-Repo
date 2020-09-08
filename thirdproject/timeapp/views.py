from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def time_view(request):
    return HttpResponse('<h1>Time View called </h1>')
