from django.db import models
from datetime import date

class Area(models.Model):
	area_tipo			= models.CharField(primary_key=True, max_length=100)
	def __str__(self):
		return self.area_tipo

class Grupo(models.Model):
	area 				= models.ForeignKey(Area, on_delete=models.CASCADE)
	codigo 				= models.CharField(max_length=100)
	numero_alumnos		= models.IntegerField(default=0)
	def __str__(self):
		return self.codigo


class Estudiante(models.Model):
	grupo 				= models.ForeignKey(Grupo, on_delete=models.CASCADE)
	nombre 				= models.CharField(max_length=100)
	apellido 			= models.CharField(max_length=100)
	fecha_nacimiento	= models.DateField()
	dni					= models.IntegerField(primary_key=True)
	def __str__(self):
		return self.nombre

class Ranking(models.Model):
	area 	 			= models.ForeignKey(Area,on_delete=models.CASCADE)
	fecha 				= models.DateField(default=date.today)
	promedio			= models.FloatField(default=0)
	def __str__(self):
		return str(self.fecha)

class Examen(models.Model):
	estudiante 			= models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	ranking 			= models.ForeignKey(Ranking,on_delete=models.CASCADE)
	fecha 				= models.DateField(default=date.today)
	nota				= models.FloatField(default=0)
	codigo				= models.CharField(max_length=100)
	def __str__(self):
		return self.codigo

class ListaAsistencia(models.Model):
	estudiante 			= models.OneToOneField(Estudiante,on_delete=models.CASCADE)
	def __str__(self):
		return self.estudiante.nombre

class RegistroDia(models.Model):
	listaAsistencia		= models.ForeignKey(ListaAsistencia,on_delete=models.CASCADE)
	fecha 				= models.DateField(default=date.today)
	def __str__(self):
	   	return str(self.fecha)

class RegistroTarde(models.Model):
	listaAsistencia		= models.ForeignKey(ListaAsistencia,on_delete=models.CASCADE)
	fecha  				= models.DateField(default=date.today)
	def __str__(self):
		return str(self.fecha)
class RegistroSeminario(models.Model):
	listaAsistencia		= models.ForeignKey(ListaAsistencia,on_delete=models.CASCADE)
	fecha 				= models.DateField(default=date.today)
	def __str__(self):
		return str(self.fecha)

