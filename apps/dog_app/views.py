# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from models import Dog


def index(request):
    dogs = Dog.objects.all()
    context = {'dogs':dogs}
    return (render(request, 'dog_app/index.html', context))


def create(request):
    print request.POST
    dog = Dog(name = request.POST['name'], breed = request.POST['breed'])
    dog.save()
    return redirect('/')

def edit(request, id):
    dog = Dog.objects.get(id=id)
    context = {"dog":dog}
    return render(request, 'dog_app/edit.html', context)

def update(request, id):
    dog = Dog.objects.get(id=id)
    dog.name = request.POST['name']
    dog.breed = request.POST['breed']
    dog.save()
    return redirect('/')

def destroy(request, id):
    dog = Dog.objects.get(id=id)
    dog.delete();
    return redirect('/')

