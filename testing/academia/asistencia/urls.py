from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login
from . import views


app_name='asistencia'
urlpatterns = [
	url(r'^$', login_required(views.index), name='index'),
	url(r'(?P<estudiante_id>[0-9]+)/$', views.estudiante, name='estudiante'),
	url(r'^pruebas',views.pruebas, name='pruebas'),
]	

"""
url(r'elegir_estudiante/$', views.Estudiante.as_view(), name='estudiante'),"""