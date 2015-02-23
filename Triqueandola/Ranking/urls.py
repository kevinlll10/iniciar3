# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from Ranking import views 

urlpatterns = patterns('', 
    url ( r'^$' , views.index , name = 'index' ),
    url ( r'^buscar/$', views.busqueda, name='busqueda'),
    url ( r'^buscar/((?P<cursoB>.+)/)?$', views.busqueda, name='busqueda' ),
    url ( r'^profesores/$', views.profesores, name='profesores'),
    url ( r'^registrar/$', views.registroEstudiante, name='registro'),
    url ( r'^login/$', views.loginRequest,name='login'),
    url ( r'^logout/$', views.logoutRequest, name = 'logout'),
    url ( r'^(?P<profesor>[\w\-]+)/$', views.datosProfesor, name='datosProfesor'),
) 