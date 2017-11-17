# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render 
from .models import User 
#from django.core.urlresolvers import reverse
from models import *


def index(request):
    return render(request, 'apt/index.html')

def process(request):
    Appointment.objects.create( 
        date = request.POST['date'], 
        time = request.POST['time'],
        task = request.POST['task'],
        )
    return redirect('/appointments')

def edit(request, user_id):
    return render(request, 'apt/edit.html')