# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Alumno(models.Model):
	"""docstring for Alumno"""
	Papellido=models.CharField(max_length=20)
	Sapellido=models.CharField(max_length=20)
	Nombres=models.CharField(max_length=20)
	DNI=models.CharField(max_length=10)
	Fechanacimiento=models.DateField()
	#SEXOS=(('F','Femenino'),'M','Masculino')
	#Sexo=models.CharField(max_length=1,choices=SEXOS,default='M')


	def NombreCompleto(self):
		cadena="{0} {1}, {2}"
		return cadena.format(self.Papellido,self.Sapellido,self.Nombres)

	def __str__(self):
		return self.NombreCompleto()

	"""def __init__(self, arg):
		super(Alumno, self).__init__()
		self.arg = arg"""

class Curso(models.Model):
	"""docstring for Curso"""

	Nombre=models.CharField(max_length=50)
	Creditos=models.PositiveSmallIntegerField()
	Estado=models.BooleanField(default=True)


	def __str__(self):
		return "{0} ({1})".format(self.Nombre,self.Creditos)


	"""def __init__(self, arg):
		super(Curso, self).__init__()
		self.arg = arg"""

class Matricula(models.Model):
	"""docstring for Matricula"""
	Alumno=models.ForeignKey(Alumno,null=False,blank=False,on_delete=models.CASCADE)
	Curso=models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
	FechaMatricula=models.DateTimeField(auto_now_add=True)


	"""def __init__(self, arg):
		super(Matricula, self).__init__()
		self.arg = arg"""
	
	def __str__(self):
		cadena="{0} => {1}"
		return cadena.format(self.Alumno,self.Curso.Nombre)


class Clientes(models.Model): # clientes 
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()
    fecha_crea = models.DateTimeField(default=timezone.now,blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    def NombreCompleto(self):
		cadena="{0} , {1}"
		return cadena.format(self.nombres,self.apellidos)

    def __str__(self):
		return self.NombreCompleto()