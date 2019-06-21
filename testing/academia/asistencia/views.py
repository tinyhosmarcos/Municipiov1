from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import *
def index(request):
	estudiantes_list = Estudiante.objects.all()


	context ={
		'estudiantes_list':estudiantes_list,
	}
	query=request.GET.get('estudiante_id')
	if query:
		estudiante = get_object_or_404(Estudiante,pk=query)
		return render(request,'asistencia/estudiante.html',{'estudiante':estudiante})
	else:
		return render(request, 'asistencia/index.html', context)
"""


class IndexView(generic.ListView):
    template_name = 'asistencia/index.html'
    context_object_name = 'estudiantes_list'

    query=request.GET.get('estudiante_id')
    
    def get_queryset(self):

    	if query:
    		return Estudiante.objects.get(pk=query)
    	else:	
        	return Estudiante.objects.all()
"""


def estudiante(request, estudiante_id):

	estudiante 	= get_object_or_404(Estudiante,pk=estudiante_id)
	return render(request, 'asistencia/estudiante.html',{'estudiante':estudiante})

