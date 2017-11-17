# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render 
from .models import User 
#from django.core.urlresolvers import reverse
#from models import *


def index(request):
    return render(request, 'main/index.html')

def register(request):
    user=User.objects.create( 
        name = request.POST['name'], 
        email = request.POST['email'],
        password = request.POST['pw'],
        birth_date = request.POST['birthday']
        )
    return redirect('/appointments')

def login(request):
    return redirect('/appointments')