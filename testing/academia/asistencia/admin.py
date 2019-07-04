from django.contrib import admin
from django.db import models
from django import forms
from .models import *



class GrupoInline(admin.TabularInline):
	model = Grupo
	extra = 2

class AreaAdmin(admin.ModelAdmin):
	fieldsets = [
		('Informacion',{'fields':['area_tipo']}),
	]
	inlines = [GrupoInline]
	list_display =('area_tipo',)

class EstudianteInline(admin.TabularInline):
	model = Estudiante
	extra = 4
	formfield_overrides = {
		models.IntegerField: {'widget': forms.NumberInput(attrs={'size': '40'})},
	}


class GrupoAdmin(admin.ModelAdmin):
	fieldsets =[
		('Area', {'fields':['area']}),
		('Information',{'fields':['codigo']}),
		(None,{'fields':['numero_alumnos']}),
	]
	inlines = [EstudianteInline]
	list_display = ('codigo', 'numero_alumnos')
	search_fields =['codigo']

class RegistroAsistenciaInline(admin.TabularInline):
	model = RegistroAsistencia
	extra = 4


class EstudianteAdmin(admin.ModelAdmin):
	fieldsets=[
		('Informacion',{'fields':['grupo']}),
		(None, {'fields':['nombre']}),
		(None, {'fields':['apellido']}),
		(None,{'fields':['fecha_nacimiento']}),
		(None,{'fields':['dni']}),
	]
	raw_id_fields = ("grupo",)
	inlines = [RegistroAsistenciaInline]
	formfield_overrides = {
		models.IntegerField: {'widget': forms.NumberInput(attrs={'size': '40'})},
	}
	list_display=('dni','nombre','apellido','fecha_nacimiento')
	search_fields=['nombre']

class ExamenInline(admin.TabularInline):
	model = Examen
	extra = 10
	raw_id_fields = ("estudiante",)

class RankingAdmin(admin.ModelAdmin):
	fieldsets=[
		('Area',{'fields':['area']}),
		('Fecha',{'fields':['fecha']}),	
	]
	inlines = [ExamenInline]
	list_display=('fecha','area','promedio')



admin.site.register(Area,AreaAdmin)
admin.site.register(Grupo,GrupoAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(RegistroAsistencia)
admin.site.register(Ranking,RankingAdmin)


admin.site.register(Examen)