from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def webpage1(request):
    dt=datetime.datetime.now()
    my_dict={'date':dt}
    return render(request, 'project5/webpage1.html', context=my_dict)

def webpage2(request):
    return render(request, 'project5/webpage2.html')

def webpage3(request):
    return render(request, 'project5/webpage3.html')
