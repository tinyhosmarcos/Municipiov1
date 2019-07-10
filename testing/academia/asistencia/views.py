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
		return redirect('asistencia:estudiante',estudiante.dni)
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

	try:
		obj=RegistroAsistencia.objects.get(estudiante=query,fecha=datetime.now().strftime("%Y-%m-%d"))
	except RegistroAsistencia.DoesNotExist:
		registro=RegistroAsistencia.objects.create(estudiante=Estudiante.objects.get(pk=query))
		registro.save()
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
		area_list=Area.objects.all()
		ranking_list=Ranking.objects.all()
		ranking_default=Ranking.objects.last()
		form=AreaForm(request.GET or None)
		query=request.GET.get('area')

		if query:
			ranking_list=Ranking.objects.filter(area=query)

		if 'ranking_get' in request.GET:
			query_ranking=request.GET.get('rankinglist_id')
			ranking_default=Ranking.objects.get(pk=query_ranking)
				
			print(query_ranking)

		if 'get_promedio' in request.GET:
			promedio_temp=0
			count=0
			query_ranking=request.GET.get('ranking_id')
			examenes=Examen.objects.filter(ranking=query_ranking)
			print(ranking_default.id)
			for examen in examenes:
				promedio_temp=promedio_temp+examen.nota
				count=count+1
			ranking_default=Ranking.objects.get(pk=query_ranking)
			ranking_default.promedio=(promedio_temp/count)
			ranking_default.save()
			print("entro_promedio")

		context={
			'ranking_list':ranking_list,
			'area_list':area_list,
			'form':form,
			'ranking_default':ranking_default,
		}
		return render(request,'asistencia/ranking.html',context)

		
def grupo(request):
		grupos_list=Grupo.objects.all()
		grupo_default=Grupo.objects.last()
		query=None
		form=AreaForm(request.GET or None)
		if form.is_valid():
			query=request.GET.get('area')
			grupos_list=Grupo.objects.filter(area=query)
		print(query)
		if 'grupo_get' in request.GET:
			query=request.GET.get('grupoid_list')
			print("grupo_get",query)
			grupo_default=Grupo.objects.get(pk=query)
		if 'set_alumnos' in request.GET:
			count=0
			query=request.GET.get('grupo_id')
			estudiantes=Estudiante.objects.filter(grupo=query)
			grupo_default=Grupo.objects.get(pk=query)
			grupo_default.numero_alumnos=estudiantes.count()
			grupo_default.save()
		context={
			'grupos_list':grupos_list,
			'form':form,
			'grupo_default':grupo_default,
		}
		return render(request,'asistencia/grupo.html',context)


















	

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