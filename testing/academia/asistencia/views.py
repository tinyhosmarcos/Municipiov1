from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *

def index(request):
	estudiantes_list = Estudiante.objects.all()
	context ={
		'estudiantes_list':estudiantes_list,
	}
	return render(request, 'asistencia/index.html', context)


def estudiante(request, estudiante_id):

	estudiante 	= get_object_or_404(Estudiante,pk=estudiante_id)
	return render(request, 'asistencia/estudiante.html',{'estudiante':estudiante})

def elegir_estudiante(request, estudiante_id):
	estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
	return render(request, 'asistencia/estudiante.html',{'estudiante':estudiante})