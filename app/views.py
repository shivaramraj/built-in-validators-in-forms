from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def Topic(request):
    TO=TopicForm()
    d={'TO':TO}

    if request.method=='POST':
        TOD=TopicForm(request.POST)
        if TOD.is_valid():
            return HttpResponse('its a valid data')
        else:
            return HttpResponse ('ITS NOT A VALID DATA')
    return render(request,'Topic.html',d)