from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario



def landing(request):
    return render(request, 'users/landing.html')


def loginsis(request):

    if request.method == 'GET':
        username=None
        username=request.user.username
        usuario = User.objects.filter(username=username).exists()
        if usuario:
            usuario = User.objects.get(username=username)
        if len(username)!=0 and not usuario.is_superuser:
            return redirect('/management/menu')

        template = loader.get_template('users/login.html')
        ctx = {
        }
        return HttpResponse(template.render(ctx,request))

    if request.method == 'POST':
        mensaje=(False,"")
        username = request.POST['username']
        password = request.POST['password']
        usuario = User.objects.filter(username=username).exists()
        if usuario:
            usuario = User.objects.get(username=username)
            if not usuario.is_superuser:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/management/menu')

                else:
                    mensaje = (True, "Contraseña invalida")
            else:
                mensaje = (True, "No existe el usuario " + username)
        else:
            mensaje = (True, "No existe el usuario " + username)


    template = loader.get_template('users/login.html')
    ctx = {'mensaje':mensaje,
            }
    return HttpResponse(template.render(ctx,request))

def register(request):

    if request.method == 'GET':

        username = None
        username = request.user.username
        usuario = User.objects.filter(username=username).exists()
        if usuario:
            usuario = User.objects.get(username=username)
        if len(username)!=0 and not usuario.is_superuser:
            return redirect('/management/menu')

        template = loader.get_template('users/register.html')
        ctx = {
        }
        return HttpResponse(template.render(ctx,request))

    if request.method == 'POST':
        
        mensaje=(False,"")
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1= request.POST.get('password1')
        password2= request.POST.get('password2')
        cc = request.POST.get('cc')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')

        usuario = User.objects.filter(username=username).exists()
        documento = Usuario.objects.filter(document=cc).exists()
        if not usuario:
            if not documento:
                if password1 == password2:
                    user = User.objects.create_user(
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password1
                    )
                    user.save()

                    usuario = Usuario.objects.create(
                            user = user,
                            document = cc,
                            fecha_nacimiento = fecha_nacimiento
                    )

                    usuario.save()

                    mensaje=(True,"Usuario registrado exitosamente")
                else:
                    mensaje=(True,"No coinciden las contraseñas")
            else:
                mensaje=(True,"Ya existe un usuario con este documento")
        else:
            mensaje=(True,"Ya existe un usuario registrado con ese nombre de usuario")

    template = loader.get_template('users/register.html')
    ctx = {'mensaje':mensaje,
            }
    return HttpResponse(template.render(ctx,request))


@login_required(login_url='/loginsis/')
def cerrarSesion(request):
    if request.user is not None:
        logout(request)
    return redirect('landing')