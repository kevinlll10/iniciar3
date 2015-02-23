# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profesor(models.Model):
	nombre = models.CharField(max_length = 70)
	puntajeP = models.DecimalField(max_digits=4,decimal_places=2,default=0)
	exigenciaP = models.DecimalField(max_digits=4,decimal_places=2,default=0)#Why default 0 :(
	pedagogiaP = models.DecimalField(max_digits=4,decimal_places=2,default=0)
	conocimientoP = models.DecimalField(max_digits=4,decimal_places=2,default=0)
	pasabilidadP = models.DecimalField(max_digits=4,decimal_places=2,default=0)
	#Comin soon : to be continued
	def __unicode__(self):
		return self.nombre

class Curso(models.Model):
	nombre = models.CharField(max_length = 70)
	ciclo = models.IntegerField()
	escuela = models.CharField(max_length = 20,default=' ')
	profesores = models.ManyToManyField(Profesor, through='Dictado')
	def __unicode__(self):
		return u"%s (%s)" %(self.nombre,self.escuela)

class Dictado(models.Model):
	curso = models.ForeignKey(Curso)
	profesor = models.ForeignKey(Profesor)

	puntajeP = models.DecimalField(max_digits=4,decimal_places=2,default=0)
	exigenciaP = models.DecimalField(max_digits=4,decimal_places=2,default=0)
	pedagogiaP = models.DecimalField(max_digits=4,decimal_places=2,default=0)
	conocimientoP = models.DecimalField(max_digits=4,decimal_places=2,default=0)	
	pasabilidadP = models.DecimalField(max_digits=4,decimal_places=2,default=0)

	def __unicode__(self):
		return (str(self.curso)+ " por "+str(self.profesor)).decode('utf-8')

class Estudiante(models.Model):
	nombre = models.CharField(max_length = 70)
	user = models.OneToOneField(User,null=True)#cuidado
	#Codigo?
	def __unicode__(self):
		return self.nombre

class Comentario(models.Model):
	contenido = models.CharField(max_length = 1000)
	autor = models.ForeignKey(Estudiante)  
	fecha = models.DateTimeField('Fecha de comentario')
	cursoDictado = models.ForeignKey(Dictado, null=True)

	exigencia = models.IntegerField(default=0)
	pedagogia = models.IntegerField(default=0)
	conocimiento = models.IntegerField(default=0)
	pasabilidad = models.IntegerField(default=0)
	def __unicode__(self):
		return (str(self.autor)+" - "+str(self.fecha)).decode('utf-8') #string sin ninguna codificación
