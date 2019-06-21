from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import *
def index(request):
	estudiantes_list = Estudiante.objects.all()

	query=request.GET.get('estudiante_id')
	if query:
		estudiante = get_object_or_404(Estudiante,pk=query)
		context ={
		'estudiantes_list':estudiantes_list,
		'estudiante':estudiante,
	}
		return render(request,'asistencia/estudiante.html',context)
	else:
		context ={
		'estudiantes_list':estudiantes_list,

	}
		return render(request, 'asistencia/index.html', context)



def estudiante(request, estudiante_id):
	estudiantes_list = Estudiante.objects.all()
	
	query=request.GET.get('estudiante_id')
	if query:
		estudiante = get_object_or_404(Estudiante,pk=query)
		context ={
		'estudiantes_list':estudiantes_list,
		'estudiante':estudiante,
	}
		return render(request,'asistencia/estudiante.html',{'estudiante':estudiante})
	else:
		context ={
		'estudiantes_list':estudiantes_list,

	}
		return render(request, 'asistencia/index.html', context)