from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login
from . import views


app_name='asistencia'
urlpatterns = [
	url(r'^$', login_required(views.index), name='index'),
	url(r'(?P<estudiante_id>[0-9]+)/$', login_required(views.estudiante), name='estudiante'),
	url(r'^pruebas',login_required(views.pruebas), name='pruebas'),
	url(r'^ranking',login_required(views.ranking), name='ranking'),
	url(r'^grupos',login_required(views.grupo),name='grupo'),
]	

"""
url(r'elegir_estudiante/$', views.Estudiante.as_view(), name='estudiante'),"""