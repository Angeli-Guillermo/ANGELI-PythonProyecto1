from django.urls import path
from AppCoder.views import *

urlpatterns = [ 
    
    path("inicio/", inicio),
    path("profesores/", profesores),
    path("cursos/", cursos),
    path("entregables/", entregables),
    path("estudiantes/", estudiantes),
    
    ]