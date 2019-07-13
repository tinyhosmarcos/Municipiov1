from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login
from . import views


app_name='asistencia'
urlpatterns = [
	url(r'^$', login_required(views.index), name='index'),
	url(r'(?P<estudiante_id>[0-9]+)/$', login_required(views.estudiante), name='estudiante'),
	url(r'^(?P<area_id>[\w\-]+)/pruebas/$',login_required(views.pruebas), name='pruebas'),
	url(r'^ranking',login_required(views.ranking), name='ranking'),
	url(r'^grupos',login_required(views.grupo),name='grupo'),
	url(r'^(?P<ranking_id>[0-9]+)/some_view/$', views.some_view,name='some_view'),
	url(r'^(?P<estudiante_id>[0-9]+)/some_asistencia/$',views.some_asistencia, name='some_asistencia'),
	url(r'^(?P<estudiante_id>[0-9]+)/some_reporte_alumno/$',views.some_reporte_alumno, name='some_reporte_alumno'),
	url(r'^(?P<area_id>[\w\-]+)/api/data/$',views.get_data,name='api-data'),
	url(r'^top/data/$',views.top_data,name='top_data'),
	url(r'^(?P<estudiante_id>[0-9]+)/api/estudiante/$',views.get_data_estudiante,name='get_data_estudiante'),
]	

"""
url(r'elegir_estudiante/$', views.Estudiante.as_view(), name='estudiante'),"""