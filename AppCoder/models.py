from django.db import models

# Create your models here.
class Estudiantes(models.Model):

 Nombre= models.CharField(max_length=30)   
 Apellidos= models.CharField(max_length=30)
 Mail= models.EmailField()

class Profesores(models.Model):

 Nombre= models.CharField(max_length=30)   
 Apellidos= models.CharField(max_length=30)
 Profesion= models.CharField(max_length=10)
 Mail= models.EmailField()

class Entregable(models.Model):

 Nombre= models.CharField(max_length=30)   
 FechaDeEntrega= models.IntegerField()
 Profesion= models.CharField(max_length=10)
 Entregado= models.CheckConstraint

class Curso(models.Model):

 Nombre= models.CharField(max_length=30)   
 Comision= models.CharField(max_length=20)