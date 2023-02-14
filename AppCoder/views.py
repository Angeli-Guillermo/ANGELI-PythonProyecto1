from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
 
def inicio(request):
    return render(request, "AppCoder/inicio.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html") 