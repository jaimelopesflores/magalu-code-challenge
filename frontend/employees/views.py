# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse

service_url = os.environ.get('SERVICE_URL')

def index(request):
    response = requests.get('%s/employee' % service_url)
    context = {'employee_list': response.json()}
    return render(request, 'employees/index.html', context)

def detail(request, id):
    response = requests.get('%s/employee/%s' % (service_url, id))
    context = {'employee': response.json()}
    return render(request, 'employees/detail.html', context)

def new(request):
    return render(request, 'employees/new.html')

def create(request):
    payload  = {
        'name': request.POST['name'] ,
        'email': request.POST['email'] ,
        'department': request.POST['department'] ,
    }
    requests.post('%s/employee' % service_url, json=payload)
    return redirect('index')

def edit(request, id):
    response = requests.get('%s/employee/%s' % (service_url, id))
    context = {'employee': response.json()}
    return render(request, 'employees/edit.html', context)

def update(request, id):
    payload  = {
        'name': request.POST['name'] ,
        'email': request.POST['email'] ,
        'department': request.POST['department'] ,
    }
    requests.put('%s/employee/%s' % (service_url, id), json=payload)
    return redirect('index')

def delete(request, id):
    requests.delete('%s/employee/%s' % (service_url, id))
    return redirect('index')
