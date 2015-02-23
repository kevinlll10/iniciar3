# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from Ranking.models import Estudiante

class RegistrationForm(ModelForm):
	usuario = forms.CharField(label=(u'Usuario'))
	correo = forms.EmailField(label=(u'Correo'))
	contrasena = forms.CharField(label=(u'Contrasena'), widget=forms.PasswordInput(render_value=False))
	contrasena1 = forms.CharField(label=(u'Verificar contrasena'), widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = Estudiante
		exclude = ('user',)

	def clean_username(self):
		usuario = self.cleaned_data['usuario']
		try:
				User.objects.get(username=usuario)
		except User.DoesNotExist:
				return usuario
		raise forms.ValidationError("Ese usuario ya existe. Por favor, utilice otro.")

	def clean(self):
		if self.cleaned_data['contrasena'] != self.cleaned_data['contrasena1']: #Ojo con esto
			raise forms.ValidationError("Las contrasenas no coinciden. Por favor, vuelva a intentar.")
		return self.cleaned_data

class LoginForm(forms.Form):
	usuario = forms.CharField(label=(u'Usuario'))
	contrasena = forms.CharField(label=(u'Contrasena'), widget=forms.PasswordInput(render_value=False))

