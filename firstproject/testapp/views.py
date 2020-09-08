from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def test_function(request):
    d=datetime.datetime.now()
    return HttpResponse('<h1>This is response from Django appp::' + str(d) + '</h1>')
