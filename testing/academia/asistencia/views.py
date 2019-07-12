from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import *
from datetime import datetime
from io import BytesIO
from reportlab.lib.colors import black
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph,Table,TableStyle
#
 
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
			'query':query,
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

def some_view(request,ranking_id):
	ranking=Ranking.objects.get(pk=ranking_id)
	examenes=Examen.objects.filter(ranking=ranking_id).order_by('-nota')

	print("Entro_some")
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="reporte_ranking.pdf"'
	buffer= BytesIO()

	# Create the PDF object, using the response object as its "file."
	c = canvas.Canvas(buffer,pagesize=A4)

	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica',22)
	c.drawString(30,750,'Academia Municipal')

	c.setFont('Helvetica',12)
	c.drawString(30,735,'Ranking Semanal: N°' + str(ranking_id))

	c.setFont('Helvetica-Bold',15)
	c.drawString(30,710,'Area: '+str(ranking.area))

	c.setFont('Helvetica-Bold',15)
	c.drawString(410,710,'Promedio Total: ' +str(ranking.promedio))

	c.setFont('Helvetica-Bold',12)
	c.drawString(450,750,"Fecha: "+str(ranking.fecha))
	c.line(440,747,560,747)

	#table header
	styles 		= getSampleStyleSheet()
	styleBH 	= styles["Normal"]
	styleBH.alignment = TA_CENTER
	styleBH.fontSize  = 10

	posicion	= Paragraph('''#''',styleBH)
	numero 		= Paragraph('''DNI''', styleBH)
	alumno 		= Paragraph('''Alumno''',styleBH)
	nota 		= Paragraph('''Nota''',styleBH)
	data=[]
	data.append([posicion, numero, alumno, nota])

	styleN		= styles["BodyText"]
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7

	high=650
	posicion_temp=1
	for examen in examenes:
		this_student = [str(posicion_temp),str(examen.estudiante.dni),str(examen.estudiante.apellido)+", "+str(examen.estudiante.nombre),str(examen.nota)]
		data.append(this_student)
		high=high-18
		posicion_temp=posicion_temp+1

	width, height = A4
	table = Table(data, colWidths=[1.9*cm, 3.61 * cm, 9.5 * cm, 4.0 * cm])	
	table.setStyle(TableStyle([
		('INNERGRID',(0,0),(-1,-1),0.25, black),
		('BOX',(0,0),(-1,-1),0.25, black),
		]))	
	table.wrapOn(c, width , height)
	table.drawOn(c, 30, high)
	c.showPage()

	c.save()
	pdf=buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response



def some_asistencia(request, estudiante_id):
	estudiante=Estudiante.objects.get(pk=estudiante_id)
	registro_asistencia=RegistroAsistencia.objects.filter(estudiante=estudiante_id)
	print("Entro_asistencia")
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="reporte_asistencia.pdf"'
	buffer= BytesIO()

	# Create the PDF object, using the response object as its "file."
	c = canvas.Canvas(buffer,pagesize=A4)

	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica',22)
	c.drawString(30,750,'Academia Municipal')

	c.setFont('Helvetica',12)
	c.drawString(30,735,'Registro de Asistencia')

	c.setFont('Helvetica-Bold',15)
	c.drawString(30,710,'Estudiante: '+str(estudiante.apellido)+", "+str(estudiante.nombre))

	c.setFont('Helvetica',12)
	c.drawString(410,710,'Area: ' +str(estudiante.grupo.area))

	c.setFont('Helvetica-Bold',12)
	c.drawString(450,750,"DNI: "+str(estudiante.dni))
	c.line(440,747,560,747)

	styles 		= getSampleStyleSheet()
	styleBH 	= styles["Normal"]
	styleBH.alignment = TA_CENTER
	styleBH.fontSize  = 10

	fecha		= Paragraph('''Fecha''',styleBH)
	dia 		= Paragraph('''Dia''', styleBH)
	tarde 		= Paragraph('''Tarde''',styleBH)
	seminario	= Paragraph('''Seminario''',styleBH)
	data=[]
	data.append([fecha, dia, tarde, seminario])

	styleN		= styles["BodyText"]
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7

	high=650
	for registro in registro_asistencia:
		this_registro = [str(registro.fecha),
		'Asistio' if registro.registro_dia else 'No',
		'Asistio' if registro.registro_tarde else 'No',
		'Asistio' if registro.registro_seminario else 'No']


		data.append(this_registro)
		high=high-18
		
	width, height = A4
	table = Table(data, colWidths=[7.5 *cm, 3.0 * cm, 3.0 * cm, 3.0 * cm])	
	table.setStyle(TableStyle([
		('INNERGRID',(0,0),(-1,-1),0.25, black),
		('BOX',(0,0),(-1,-1),0.25, black),
		]))	
	table.wrapOn(c, width , height)
	table.drawOn(c, 30, high)
	c.showPage()

	c.save()
	pdf=buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response


def pruebas(request,area_id):
	 print(area_id)
	 return render(request, 'asistencia/testing.html',{'area_id':area_id}
	 	)

def get_data(request,area_id):
	ranking_list=Ranking.objects.filter(area=area_id).order_by('fecha')
	labels=[]
	default_items=[]
	for ranking in ranking_list:
		labels.append(str(ranking.fecha))
		default_items.append(str(ranking.promedio))

	#labels=['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
	#default_items=[12,18,13,14,15,16]
	data ={
		"labels":labels,
		"default":default_items,
	}
	return JsonResponse(data)


