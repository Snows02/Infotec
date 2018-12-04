from management.views import *
from users.views import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


@login_required(login_url='/login/')
def menu(request):
    if request.method == 'GET':
        username=None
        username=request.user.username
        usuario = User.objects.filter(username=username)


        template = loader.get_template('management/menu.html')
        ctx = {'usuario':usuario,
        }
        return HttpResponse(template.render(ctx,request))

def gotodiagnostico(request):
    if request.method == 'GET':
        username=None
        username=request.user.username
        usuario = User.objects.filter(username=username)


        template = loader.get_template('management/diagnostico.html')
        ctx = {'usuario':usuario,
        }
        return HttpResponse(template.render(ctx,request))
    if request.method == 'POST':
        opcion1 = request.POST.get('respuesta1')
        opcion2 = request.POST.get('respuesta2')
        opcion3 = request.POST.get('respuesta3')
        opcion4 = request.POST.get('respuesta4')
        opcion5 = request.POST.get('respuesta5')
        opcion6 = request.POST.get('respuesta6')
        opcion7 = request.POST.get('respuesta7')
        opcion8 = request.POST.get('respuesta8')

        

        '''Para sifilis'''
        if opcion1=="2" and opcion2=="1" and opcion3=="0" and opcion4=="0" and opcion5=="0" and opcion6=="0" and opcion7=="0" and opcion8=="0" or opcion1=="0" and opcion2=="1" and opcion3=="0" and opcion4=="0" and opcion5=="0" and opcion6=="0" and opcion7=="0" and opcion8=="0" or opcion1=="1" and opcion2=="1" and opcion3=="0" and opcion4=="0" and opcion5=="0" and opcion6=="0" and opcion7=="0" and opcion8=="0" :
            print("Sifilis etapa 1")
            enfermedad=("La probabilidad que usted tenga sifilis etapa 1 es de de 80%")
        if opcion2=="1" and opcion3=="1" and opcion1=="0" and opcion4=="0" and opcion5=="0" and opcion6=="0" and opcion7=="0" and opcion8=="0" or opcion1=="1" and opcion2=="1" and opcion3=="1" and opcion4=="0" and opcion5=="0" and opcion6=="0" and opcion7=="0" and opcion8=="0":
            enfermedad=("La probabilidad que usted tenga sifilis etapa 2 es de 80%")
        
        '''Para gonorrea'''
        if opcion4=="1" and opcion5=="1" and opcion6=="1" or opcion4=="1" and opcion5=="1" and opcion6=="0" or opcion4=="1" and opcion5=="0" and opcion6=="1":
            enfermedad=("La probilidad que usted tenga gonorrea es de 80%")
        if opcion4=="1" and opcion5=="1" and opcion6=="0" or opcion4=="1" and opcion5=="0" and opcion6=="1":
            enfermedad= ("La probabilidad que usted tenga gonorrea es de 70% ")
        
        '''Para VPH'''
        if opcion7=="1" and opcion8=="1" or opcion7=="1" and opcion8=="2":
            enfermedad=("la probabilidad que usted tenga el virus del papiloma humano es de 60%")
        if opcion7 =="1" and opcion8=="0":
            enfermedad=("la probalidad que usted tenga el virus del papiloma humano es de menos de 50%")
        
        template = loader.get_template('management/resultados.html')

        ctx = {'enfermedad':enfermedad,
        }
        return HttpResponse(template.render(ctx,request))
