from django.contrib import admin

from .models import *

admin.site.register(Area)
admin.site.register(Estudiante)
admin.site.register(Grupo)
admin.site.register(Ranking)
admin.site.register(ListaAsistencia)
admin.site.register(RegistroDia)
admin.site.register(RegistroTarde)
admin.site.register(RegistroSeminario)
admin.site.register(Examen)