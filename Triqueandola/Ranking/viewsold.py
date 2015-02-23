# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.template import RequestContext, loader
from Ranking.models import *

def index(request):
	profesores = Profesor.objects.all()
	profesores = profesores[len(profesores)-4:len(profesores)]

	comentarios = Comentario.objects.all()
	comentarios = comentarios[len(comentarios)-4:len(comentarios)]

	rankingExi = profesores
	inter=len(rankingExi)
    cant = len(rankingExi)
    while inter>=1:
        inter = inter/2
        flag=True
        while flag:
            flag=False
            i=0
            while i+inter<cant:
                if rankingExi[i].exigenciaP>rankingExi[i+inter].exigenciaP:
                    aux=rankingExi[i]
                    rankingExi[i]=rankingExi[i+inter]
                    rankingExi[i+inter]=aux
                    flag=True
                i+=1

    lon = len(rankingExi)
    rankingExiMen = rankingExi[lon/3-3:lon/3]
    rankingExiMed = rankingExi[2*lon/3-3:2*lon/3]
    rankingExiMay = rankingExi[lon-3:lon]
    
    rankingExi=list()
    rankingExi.append(rankingExiMen)
    rankingExi.append(rankingExiMed)
    rankingExi.append(rankingExiMay)



	rankingPas = profesores
	inter=len(rankingPas)
    cant = len(rankingPas)
    while inter>=1:
        inter = inter/2
        flag=True
        while flag:
            flag=False
            i=0
            while i+inter<cant:
                if rankingPas[i].pasabilidadP>rankingPas[i+inter].pasabilidadP:
                    aux=rankingPas[i]
                    rankingPas[i]=rankingPas[i+inter]
                    rankingPas[i+inter]=aux
                    flag=True
                i+=1	
    lon = len(rankingPas)
    rankingPasMen = rankingPas[lon/3-3:lon/3]
    rankingPasMed = rankingPas[2*lon/3-3:2*lon/3]
    rankingPasMay = rankingPas[lon-3:lon]
    
    rankingPas=list()
    rankingPas.append(rankingPasMen)
    rankingPas.append(rankingPasMed)
    rankingPas.append(rankingPasMay)



	rankingCon = profesores
	inter=len(rankingCon)
    cant = len(rankingCons)
    

    while inter>=1:
        inter = inter/2
        flag=True
        while flag:
            flag=False
            i=0
            while i+inter<cant:
                if rankingCon[i].conocimientoP>rankingCon[i+inter].conocimientoP:
                    aux=rankingCon[i]
                    rankingCon[i]=rankingCon[i+inter]
                    rankingCon[i+inter]=aux
                    flag=True
                i+=1	
    lon = len(rankingCon)
    rankingConMen = rankingCon[lon/3-3:lon/3]
    rankingConMed = rankingCon[2*lon/3-3:2*lon/3]
    rankingConMay = rankingCon[lon-3:lon]
    
    rankingCon=list()
    rankingCon.append(rankingConMen)
    rankingCon.append(rankingConMed)
    rankingCon.append(rankingConMay)


	rankingPed = profesores
	inter=len(rankingPed)

    while inter>=1:
        inter = inter/2
        flag=True
        while flag:
            flag=False
            i=0
            while i+inter<cant:
                if rankingPed[i].pedagogia>rankingPed[i+inter].pedagogia:
                    aux=rankingPed[i]
                    rankingPed[i]=rankingPed[i+inter]
                    rankingPed[i+inter]=aux
                    flag=True
                i+=1

    lon = len(rankingPed)
    rankingPedMen = rankingPed[lon/3-3:lon/3]
    rankingPedMed = rankingPed[2*lon/3-3:2*lon/3]
    rankingPedMay = rankingPed[lon-3:lon]
    
    rankingPed=list()
    rankingPed.append(rankingPedMen)
    rankingPed.append(rankingPedMed)
    rankingPed.append(rankingPedMay)



	rankings = list()
	rankings.append(rankingExi)
	rankings.append(rankingPas)
	rankings.append(rankingCon)
	rankings.append(rankingExp)

	context = RequestContext(request,{'profesoresOrdenados':profesores,'comentarios':comentarios, 'rankings':rankings})
	template = loader.get_template('Ranking/home.html')
	return HttpResponse(template.render(context))



def datosProfesor(request, profesor):
	profesores = Profesor.objects.all()
	found = False
	lon = len(profesores)
	i=0
	response = HttpResponse("Yiyi profe")#Hay que preparar una página de error 404
	while i<lon and not found:
		if profesor.lower() == profesores[i].nombre.lower().replace(' ','-'): #profesor no debe tener ' '
			found = True
		else:
			i+=1
	if found:
		template = loader.get_template('Ranking/perfilProfesor.html')
		context = RequestContext(request,{'profesor':profesores[i]})
		response = HttpResponse(template.render(context))

	query = request.POST
	#Sé que habrá valores por defecto
	
	print query
	return response


def dictadosProfesor(request, profesor,curso):
	profesores = Profesor.objects.all()
	found = False
	lon = len(profesores)
	i=0
	while i<lon and not found:
		if profesor.lower() == profesores[i].nombre.lower(): #profesor no debe tener ' '
			found = True
		else:
			i+=1
	if found:
		found = False
		dictados = profesores[i].dictado_set.all()
		i=0
		lon = len(dictados)
		curso = curso.lower().replace('-',' ')
		equivalencias = list()
		while i<lon:
			if curso == dictados[i].curso.nombre.lower():
				equivalencias.append(dictados[i])
			i+=1
		template = loader.get_template('Ranking/cursosProfesor.html')
		context = RequestContext(request,{'cursosProfesor':equivalencias})
		return HttpResponse(template.render(context))
	else:
		return HttpResponse("No se encontró el profesor especificado")

def shell(lista,cant):
    inter=cant
    while inter>=1:
        inter = inter/2
        flag=True
        while flag:
            flag=False
            i=0
            while i+inter<cant:
                if lista[i]>lista[i+inter]:
                    aux=lista[i]
                    lista[i]=lista[i+inter]
                    lista[i+inter]=aux
                    flag=True
                i+=1


    