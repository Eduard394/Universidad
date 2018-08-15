# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

"""

def login_(request):
    
    return render(request, 'welcome.html', {})



def inicio(request):
    
    return render(request, 'welcome.html', {})
"""

def foo(request):
	return render(request, 'welcome.html')
    #return HttpResponse("Hello World!")


def index(request):
    
    return render(request, 'welcome.html', {})