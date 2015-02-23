# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from Ranking.forms import RegistrationForm, LoginForm
from django.shortcuts import render,render_to_response
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from Ranking.models import *
from django.contrib.auth import authenticate, login, logout

def index(request):
	profesores = Profesor.objects.all()
	profesores = profesores[len(profesores)-4:len(profesores)]

	comentarios = Comentario.objects.all()
	comentarios = comentarios[len(comentarios)-4:len(comentarios)]


	#restaurando
	profesores=Profesor.objects.all()


	rankingExi = profesores[0:len(profesores)]
	rankingExi = ordenarExigencia(rankingExi)

	lon = len(rankingExi)
	rankingExiMen=rankingExi[lon/3-3:lon/3]
	rankingExiMed=rankingExi[2*lon/3-3:2*lon/3]
	rankingExiMay=rankingExi[lon-3:lon]
	rankingExi=dict()
	rankingExi['menores']=rankingExiMen
	rankingExi['medianos']=rankingExiMed
	rankingExi['mayores']=rankingExiMay


	rankingPas = profesores[0:len(profesores)]
	rankingPas = ordenarPasabilidad(rankingPas)

	lon = len(rankingPas)
	rankingPasMen=rankingPas[lon/3-3:lon/3]
	rankingPasMed=rankingPas[2*lon/3-3:2*lon/3]
	rankingPasMay=rankingPas[lon-3:lon]
	rankingPas=dict()
	rankingPas['menores']=rankingPasMen
	rankingPas['medianos']=rankingPasMed
	rankingPas['mayores']=rankingPasMay


	rankingCon = profesores[0:len(profesores)]
	rankingCon = ordenarConocimiento(rankingCon)

	lon = len(rankingCon)
	rankingConMen=rankingCon[lon/3-3:lon/3]
	rankingConMed=rankingCon[2*lon/3-3:2*lon/3]
	rankingConMay=rankingCon[lon-3:lon]
	rankingCon=dict()
	rankingCon['menores']=rankingConMen
	rankingCon['medianos']=rankingConMed
	rankingCon['mayores']=rankingConMay



	rankingPed = profesores[0:len(profesores)]
	rankingPed = ordenarPedagogia(rankingPed)

	lon = len(rankingPed)
	rankingPedMen=rankingPed[lon/3-3:lon/3]
	rankingPedMed=rankingPed[2*lon/3-3:2*lon/3]
	rankingPedMay=rankingPed[lon-3:lon]
	rankingPed=dict()
	rankingPed['menores']=rankingPedMen
	rankingPed['medianos']=rankingPedMed
	rankingPed['mayores']=rankingPedMay


	rankings = dict()
	rankings['exigencia']=rankingExi
	rankings['pasabilidad']=rankingPas
	rankings['conocimiento']=rankingCon
	rankings['pedagogia']=rankingPed


	profesoresTop = profesores[len(profesores)-4:len(profesores)]
	context = RequestContext(request,{'profesoresOrdenados':profesoresTop,'comentarios':comentarios, 'rankings':rankings})
	template = loader.get_template('Ranking/home.html')
	return HttpResponse(template.render(context))

def datosProfesor(request, profesor):
	profesores = Profesor.objects.all()
	found = False
	lon = len(profesores)
	i=0
	while i<lon and not found:
		if profesor.lower() == profesores[i].nombre.lower().replace(' ','-'): #profesor no debe tener ' '
			found = True
		else:
			i+=1


	if found:
		template = loader.get_template('Ranking/profesorPerfil.html')
		context = RequestContext(request,{'profesor':profesores[i]})

		print i
		print profesores[i]
		print profesores
		if request.POST:
			print request.POST
			print str(request.user) 
			#buscando curso
			done=False
			for dictado in profesores[i].dictado_set.all():
				if dictado.curso.nombre.lower() == request.POST.get('curso').lower():
					done=True
					dictado.comentario_set.create(contenido=request.POST.get('contenido'),autor=User.objects.get(username=str(request.user)).estudiante, fecha=timezone.now(),exigencia=request.POST.get('exigencia'),pedagogia=request.POST.get('pedagogia'),pasabilidad=request.POST.get('pasabilidad'),conocimiento=request.POST.get('conocimiento'))
			if done:
				for dictado in profesores[i].dictado_set.all():
					promediarDictado(dictado)
					dictado.save()

				promediarProfesor(profesores[i])
				profesores[i].save()			
		 		return HttpResponse("exitoasda")
			else:
				return HttpResponse("YIYII")
	 	else:
	 		return HttpResponse(template.render(context))


	else:
		return HttpResponse("yiyi")		

	

def promediarDictado(dictado):
	comentarios = dictado.comentario_set.all()
	print "LONGITUD : ",len(comentarios)
	exP,paP,coP,peP=0,0,0,0
	for comentario in comentarios:
		exP+=comentario.exigencia
		paP+=comentario.pasabilidad
		coP+=comentario.conocimiento
		peP+=comentario.pedagogia
	dictado.exigenciaP=exP/len(comentarios)
	dictado.pasabilidadP=paP/len(comentarios)
	dictado.conocimientoP=coP/len(comentarios)
	dictado.pedagogiaP=peP/len(comentarios)
	dictado.puntajeP=(dictado.exigenciaP+dictado.pasabilidadP+dictado.conocimientoP+dictado.pedagogiaP)/4

#Falta save

def promediarProfesor(profesor):
	dictados = profesor.dictado_set.all()
	exP,paP,coP,peP,puP=0,0,0,0,0
	for dictado in  dictados:
		exP+=dictado.exigenciaP
		paP+=dictado.pasabilidadP
		coP+=dictado.conocimientoP
		peP+=dictado.pedagogiaP
		puP+=dictado.puntajeP
	
	profesor.exigenciaP=exP/len(dictados)
	profesor.pasabilidadP=paP/len(dictados)
	profesor.conocimientoP=coP/len(dictados)
	profesor.pedagogiaP=peP/len(dictados)
	profesor.puntajeP=puP/len(dictados)

def profesores(request):
	profesores = Profesor.objects.all()

	rankingExi = profesores[0:len(profesores)]
	rankingExi = ordenarExigencia(rankingExi)
	rankingExi = rankingExi[len(rankingExi)-4:len(rankingExi)]

	rankingPas = profesores[0:len(profesores)]
	rankingPas = ordenarPasabilidad(rankingPas)
	rankingPas = rankingPas[len(rankingPas)-4:len(rankingPas)]


	rankingCon = profesores[0:len(profesores)]
	rankingCon = ordenarConocimiento(rankingCon)
	rankingCon = rankingCon[len(rankingCon)-4:len(rankingCon)]

	rankingPed = profesores[0:len(profesores)]
	rankingPed = ordenarPedagogia(rankingPed)
	rankingPed = rankingPed[len(rankingPed)-4:len(rankingPed)]


	rankings = dict()
	rankings['exigencia']=rankingExi
	rankings['pasabilidad']=rankingPas
	rankings['conocimiento']=rankingCon
	rankings['pedagogia']=rankingPed


	template = loader.get_template('Ranking/profesores.html')
	context = RequestContext(request,{'rankings':rankings})
	return HttpResponse(template.render(context))

#def dictadosProfesor(request, profesor,curso):
#	profesores = Profesor.objects.all()
#	found = False
#	lon = len(profesores)
#	i=0
#	while i<lon and not found:
#		if profesor.lower() == profesores[i].nombre.lower(): #profesor no debe tener ' '
#			found = True
#		else:
#			i+=1
#	if found:
#		found = False
#		dictados = profesores[i].dictado_set.all()
#		i=0
#		lon = len(dictados)
#		curso = curso.lower().replace('-',' ')
#		equivalencias = list()
#		while i<lon:
#			if curso == dictados[i].curso.nombre.lower():
#				equivalencias.append(dictados[i])
#			i+=1
#		template = loader.get_template('Ranking/cursosProfesor.html')
#		context = RequestContext(request,{'cursosProfesor':equivalencias})
#		return HttpResponse(template.render(context))
#	else:
#		return HttpResponse("No se encontró el profesor especificado")

def busqueda(request,cursoB=""):

	#Parte del template : constante
	cursosTotales = Curso.objects.all()
	cursosTotales = cursosTotales[0:len(cursosTotales)]
	cursos = dict()
	software = list()
	sistemas = list()

	inter=len(cursosTotales)
	cant=len(cursosTotales)
	while inter>=1:
		inter = inter /2
		flag=True
		while flag:
			flag=False
			i=0
			while i+inter<cant:
				if cursosTotales[i].ciclo>cursosTotales[i+inter].ciclo:
					aux=cursosTotales[i]
					cursosTotales[i]=cursosTotales[i+inter]
					cursosTotales[i+inter]=aux
					flag=True
				i+=1

	for ciclo in range(10):
		software.append(list())
		sistemas.append(list())

	for curso in cursosTotales:
		if curso.escuela.lower() == 'software':
			software[curso.ciclo-1].append(curso)
		else:
			if curso.escuela.lower() == 'sistemas':
				sistemas[curso.ciclo-1].append(curso)


	cursos['software']=software
	cursos['sistemas']=sistemas



	rankings = dict()
	if request.GET:
		print request.GET
		busqueda = request.GET.get('busqueda','')
		if busqueda:
			busqueda = limpiarCadena(busqueda)
			profesores = Profesor.objects.all()
			resultados = list()
			for profesor in profesores:
				if busqueda.lower() in profesor.nombre.lower():
					resultados.append(profesor)
		#Se supone que no hay else...la validación html
		
		if resultados:
			rankings['generales']=resultados
			rankings['exigencia']=ordenarExigencia(resultados)		
			rankings['pasabilidad']=ordenarPasabilidad(resultados)		
			rankings['conocimiento']=ordenarConocimiento(resultados)		
			rankings['pedagogia']=ordenarPedagogia(resultados)

	else:
		if cursoB:
			#Quizás otro tipo de búsqueda...
			found = False
			i=0

			resultado = object()
			while (i<len(software) or i<len(sistemas)) and not found:
				j=0
				while j<len(software[i]) and not found:
					if software[i][j].nombre.lower() == cursoB.lower():
						found = True 
						resultado = software[i][j] #Bug cuando se trate de cálculo i o mate básica...
					j+=1
				
				j=0
				while j<len(sistemas[i]) and not found:
					if sistemas[i][j].nombre.lower() == cursoB.lower():
						found = True
						resultado = sistemas[i][j]
					
					j+=1

				i+=1

			#Se supone que siempre encontrará...
			resultados = list()
			for dictado in resultado.dictado_set.all():
				resultados.append(dictado.profesor)

			if resultados:
				rankings['generales']=resultados
				rankings['exigencia']=ordenarExigencia(resultados)		
				rankings['pasabilidad']=ordenarPasabilidad(resultados)		
				rankings['conocimiento']=ordenarConocimiento(resultados)		
				rankings['pedagogia']=ordenarPedagogia(resultados)
		#Se supone que siempre existirá...
		else:
			profesores = Profesor.objects.all()
			profesores = profesores[0:len(profesores)]
			rankings['generales']=profesores
			rankings['exigencia']=ordenarExigencia(profesores)		
			rankings['pasabilidad']=ordenarPasabilidad(profesores)		
			rankings['conocimiento']=ordenarConocimiento(profesores)		
			rankings['pedagogia']=ordenarPedagogia(profesores)
	template = loader.get_template('Ranking/busqueda.html')
	context = RequestContext(request,{'cursos':cursos,'rankings':rankings})
	return HttpResponse(template.render(context))

def registroEstudiante(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('#')

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			try:
				usuario = User.objects.create_user(username=form.cleaned_data['usuario'], email=form.cleaned_data['correo'], password= form.cleaned_data['contrasena'])
				usuario.save()
				estudiante = Estudiante(user=usuario, nombre=form.cleaned_data['nombre'])
				estudiante.save()
				return HttpResponse('Exito!') #Exito!
			except IntegrityError as e:
				return HttpResponse('Integrity Error  '+e.message)
			##CUIDADO
		else:
			context = RequestContext(request,{'form':form})
			template = loader.get_template('Ranking/registrar.html')
			return HttpResponse(template.render(context)) 
	else:
		form=RegistrationForm()
		template = loader.get_template('Ranking/registrar.html')
		context = RequestContext(request,{'form':form})
		return HttpResponse(template.render(context))

def loginRequest(request):
	if request.user.is_authenticated():
		return HttpResponse('PUM')

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['usuario']
			contrasena = form.cleaned_data['contrasena']
			estudiante = authenticate(username=usuario, password=contrasena)
			if estudiante is not None:
				login(request,estudiante)
				return HttpResponse('Exitooo')
			else:
				context = RequestContext(request,{'form':form})
				template = loader.get_template('Ranking/login.html')
				return HttpResponse(template.render(context))

		else:
			context = RequestContext(request,{'form':form})
			template = loader.get_template('Ranking/login.html')
			return HttpResponse(template.render(context))
	
	else:
		form = LoginForm()
		context = RequestContext(request,{'form':form})
		template = loader.get_template('Ranking/login.html')
		return HttpResponse(template.render(context))

def logoutRequest(request):
	logout(request)
	HttpResponse('exitooo')


def limpiarCadena(cadena):
	cadenaFinal=""
	invalidos = [' ','\n','\t']
	for char in cadena:
		if not char in invalidos:
			cadenaFinal+=char
	return cadenaFinal

def ordenarExigencia(profesores):
	inter=len(profesores)
	cant=len(profesores)
	while inter>=1:
		inter = inter /2
		flag=True
		while flag:
			flag=False
			i=0
			while i+inter<cant:
				if profesores[i].exigenciaP>profesores[i+inter].exigenciaP:
					aux=profesores[i]
					profesores[i]=profesores[i+inter]
					profesores[i+inter]=aux
					flag=True
				i+=1
	return profesores

def ordenarPasabilidad(profesores):
	inter=len(profesores)
	cant=len(profesores)
	while inter>=1:
		inter = inter /2
		flag=True
		while flag:
			flag=False
			i=0
			while i+inter<cant:
				if profesores[i].pasabilidadP>profesores[i+inter].pasabilidadP:
					aux=profesores[i]
					profesores[i]=profesores[i+inter]
					profesores[i+inter]=aux
					flag=True
				i+=1
	return profesores

def ordenarConocimiento(profesores):
	inter=len(profesores)
	cant=len(profesores)
	while inter>=1:
		inter = inter /2
		flag=True
		while flag:
			flag=False
			i=0
			while i+inter<cant:
				if profesores[i].conocimientoP>profesores[i+inter].conocimientoP:
					aux=profesores[i]
					profesores[i]=profesores[i+inter]
					profesores[i+inter]=aux
					flag=True
				i+=1
	return profesores

def ordenarPedagogia(profesores):
	inter=len(profesores)
	cant=len(profesores)
	while inter>=1:
		inter = inter /2
		flag=True
		while flag:
			flag=False
			i=0
			while i+inter<cant:
				if profesores[i].pedagogiaP>profesores[i+inter].pedagogiaP:
					aux=profesores[i]
					profesores[i]=profesores[i+inter]
					profesores[i+inter]=aux
					flag=True
				i+=1
	return profesores

