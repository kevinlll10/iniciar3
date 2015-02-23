# -*- coding: utf-8 -*-
from django.contrib import admin
from Ranking.models import *

class CursoDictadoInLine(admin.TabularInline):
	model = Dictado

class ProfesorAdmin(admin.ModelAdmin):
	fieldsets = [
		('Nombre',{'fields':[('nombre')]}),
	]
	inlines = [CursoDictadoInLine]


class ComentarioInLine(admin.TabularInline):
	model = Comentario


class EstudianteAdmin(admin.ModelAdmin):
	fieldsets = [
		('Nombre',{'fields':[('nombre')]}),
	]
	inlines = [ComentarioInLine]

class CursoAdmin(admin.ModelAdmin):
	ordering=('-nombre',)
	list_display=('nombre',)



admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
