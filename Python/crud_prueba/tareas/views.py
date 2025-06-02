from django.shortcuts import render
from.models import tareas
from crud_prueba.tareas.models import Tareas


# Create your views here.
def listar_tareas(request):
    tareas = Tareas.objects.all()
    return render(request,'listar_tareas.html',{'tareas':tareas})