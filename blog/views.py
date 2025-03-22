from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UsernameField
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from . import models
from . import forms
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def registro(request):
    if request.method == 'GET':
        return render(request,'registro.html',{'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                print(request.POST)
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('inicio')
            except IntegrityError:
                return render(request,'registro.html',{'form': UserCreationForm,'error':"El usurio ya existe"})
        else:
            return render(request,'registro.html',{'form': UserCreationForm,'error':"Invalid password"})
    

def salir(request):
    logout(request)
    return redirect('inicio')

def log_in(request):
    if request.method == 'GET':
        return render(request,'login.html',)
    else:
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is not None:
            print(user)
            login(request,user)
            return redirect('inicio')
        else:
            return render(request,'login.html',{'error':"Usuario o Contraseña erronea"})

def about(request):
    return render(request,'about.html')


@login_required(login_url='login')
def tareas(request):
            #try:
            tasks = models.tareas.objects.filter(usuario_id=request.user.id)
            #print(tasks)
            return render(request,'tareas.html',{'tasks':tasks})
            #except:
                #return render(request,'tareas.html',{'error':'No hay tareas creadas'})
            
        
@login_required(login_url='login')
def add_task(request):
    formu = forms.form_tareas()
    if request.method == 'GET':
        
        return render(request,'add_task.html',{'form': formu,'mode':'Agregar nueva tarea'})
    else:
        
        print(request.POST)
        db = models.tareas.objects.filter(title=request.POST['title'].strip(),usuario_id=request.user.id)
        if not db:
            models.tareas.objects.create(title=request.POST['title'].strip(),description=request.POST['description'],available=request.POST.get('available', False)=='on',usuario_id=request.user.id)
        else:
            return render(request,'add_task.html',{'form': formu,'error':"Ya existe una tarea con ese nombre",'mode':'Agregar nueva tarea'})          
        return redirect('tareas')
    
@login_required(login_url='login')
def delete_task(request,db):
    tarea = models.tareas.objects.get(title=db,usuario_id=request.user.id)
    print('Tarea = ', tarea)
    tarea.delete()
    return redirect('tareas')

@login_required(login_url='login')
def edit_task(request,db):
    tarea = models.tareas.objects.get(title=db,usuario_id=request.user.id)
    if request.method == 'GET':
        formu = forms.form_tareas(initial={'title':tarea.title,'description':tarea.description,'available':tarea.available})
        return render(request,'add_task.html',{'form': formu,'mode':'Editar tarea'})
    else:
        print('cambio')
        tarea.title = request.POST["title"]
        tarea.description = request.POST["description"]
        tarea.available = request.POST.get('available', False)=='on'
        print(tarea.title,',',tarea.description,',',tarea.available)
        tarea.save()
        return redirect('tareas')


@login_required(login_url='login')
def info_task(request,tk):
    print(tk)
    tarea = models.tareas.objects.get(title=tk)
    
    return render(request,'info_task.html',{'tarea': tarea})


def basedatos(request,ids):
    task = models.task.objects.get(id=ids)
    project = models.project_model.objects.get(id=task.project_model_id)
    return HttpResponse("<h1>La tarea : {0} tiene de titulo : {1} </h1>".format(task.title,project.name))

def proyectos(request):
    proj = models.project_model.objects.all()
    print(proj)
    return render(request,'proyectos.html',{'proj':proj})

def task(request,proj):
    project = models.project_model.objects.get(name=proj)
    pro = models.task.objects.filter(project_model=project.id)
    print(pro)
    return render(request,'task.html',{'pro':pro, 'proj':proj})

def create_task(request,tipo):
    if request.method == 'GET':
        if tipo == 'proyectos':
            formu = forms.form_project()
        else:
            print(models.project_model.objects.all())
            formu = forms.form_task()
        return render(request,'create_task.html',{'form': formu})
    else:
        print(request.POST)
        if tipo == 'proyectos':
            models.project_model.objects.create(name=request.POST['name'])
        else:
            models.task.objects.create(title=request.POST['title'],description=request.POST['description'],project_model_id=int(request.POST['project']))
        return redirect('proyectos')