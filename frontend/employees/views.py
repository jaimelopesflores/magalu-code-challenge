# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests

def index(request):
    response = requests.get('http://localhost:8000/employee')
    context = {'employee_list': response.json()}
    return render(request, 'employees/index.html', context)

def detail(request, id):
    response = requests.get('http://localhost:8000/employee/%s' % id)
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
    requests.post('http://localhost:8000/employee', json=payload)
    return redirect('index')

def edit(request, id):
    response = requests.get('http://localhost:8000/employee/%s' % id)
    context = {'employee': response.json()}
    return render(request, 'employees/edit.html', context)

def update(request, id):
    payload  = {
        'name': request.POST['name'] ,
        'email': request.POST['email'] ,
        'department': request.POST['department'] ,
    }
    requests.put('http://localhost:8000/employee/%s' % id, json=payload)
    return redirect('index')

def delete(request, id):
    requests.delete('http://localhost:8000/employee/%s' % id)
    return redirect('index')
