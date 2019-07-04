from django.shortcuts import render,redirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import *
from datetime import datetime 
def index(request):
	estudiantes_list = Estudiante.objects.all()
	print("index")
	query=request.GET.get('estudiante_id')

	if query:
		print("index_entro")
		estudiante = get_object_or_404(Estudiante,pk=query)
		return redirect('asistencia:estudiante',estudiante)
	else:
		print("index_else")
		context ={
		'estudiantes_list':estudiantes_list,
		}
		return render(request, 'asistencia/index.html', context)



def estudiante(request, estudiante_id):
	estudiantes_list = Estudiante.objects.all()
	query=request.GET.get('estudiante_id')
	if query==None and estudiante_id:
		query=estudiante_id

	obj=RegistroAsistencia.objects.get(estudiante=query,fecha=datetime.now().strftime("%Y-%m-%d"))
	print(query)
	print(estudiante_id)
	form=AsistenciaForm(request.POST or None,instance=obj)
	
	
	if request.method==("POST" or None):
		print("entro_post")
		estudiante_object = get_object_or_404(Estudiante,pk=query)
		context ={
			'estudiantes_list':estudiantes_list,
			'estudiante':estudiante_object,
			'form':form,
			}
		if form.is_valid():
			print("entro")
			form.save()
			form=AsistenciaForm()

		elif form.non_field_errors():
			data=request.POST.copy()
			fecha=data.get('fecha')
			data_estudiante=data.get('estudiante')
			registro=RegistroAsistencia.objects.get(estudiante=data_estudiante,fecha=fecha)
			data_dia=data.get('registro_dia')
			data_tarde=data.get('registro_tarde')
			data_seminario=data.get('registro_seminario')
			registro.registro_dia= True if data_dia=="on" else False
			registro.registro_tarde= True if data_tarde=="on" else False
			registro.registro_seminario= True if data_seminario=="on" else False	
			registro.save()	
		return render(request,'asistencia/estudiante.html',context)		
	if query:
		print("hello")
		estudiante = get_object_or_404(Estudiante,pk=query)
		context ={
			'estudiantes_list':estudiantes_list,
			'estudiante':estudiante,
			'form':form,
			}	
		return render(request,'asistencia/estudiante.html',context)
	else:
		context ={
		'estudiantes_list':estudiantes_list,
		}
		return render(request, 'asistencia/index.html', context)
	
		
def ranking(request):
		ranking_list=Ranking.objects.all()
		print(ranking)
		context={
			'ranking_list':ranking_list,
		}
		return render(request,'asistencia/ranking.html',context)

















	

def pruebas(request):


	estudiantes_list = Estudiante.objects.all()

	obj=RegistroAsistencia.objects.get(estudiante="72386701",fecha=datetime.now().strftime("%Y-%m-%d"))

	form=AsistenciaForm(request.POST or None,instance=obj)
	context={
		'estudiantes_list':estudiantes_list,
		'form':form,
	}
	if form.is_valid():
		
		form.save()
		form=AsistenciaForm()

	elif form.non_field_errors():
		data=request.POST.copy()
		fecha=data.get('fecha')
		estudiante=data.get('estudiante')
		registro=RegistroAsistencia.objects.get(estudiante=estudiante,fecha=fecha)
		data_dia=data.get('registro_dia')
		data_tarde=data.get('registro_tarde')
		data_seminario=data.get('registro_seminario')

		registro.registro_dia= True if data_dia=="on" else False
		registro.registro_tarde= True if data_tarde=="on" else False
		registro.registro_seminario= True if data_seminario=="on" else False	

		registro.save()

	return render(request,'asistencia/testing.html',context)