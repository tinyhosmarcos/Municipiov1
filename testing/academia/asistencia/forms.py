from django import forms
from .models import *
class AsistenciaForm(forms.ModelForm):
	class Meta:
		model = RegistroAsistencia
		fields =[
			'estudiante',
			'fecha',
			'registro_dia',
			'registro_tarde',
			'registro_seminario'
		]
		widgets={
			'estudiante': forms.TextInput(attrs={'class':'input', 'style':'display:none'	}),
			'fecha': forms.TextInput(attrs={'class':'datepicker'	}),
			'registro_dia': forms.CheckboxInput (attrs={'class':'filled-in'	}),
			'registro_tarde': forms.CheckboxInput (attrs={'class':'filled-in'	}),
			'registro_seminario': forms.CheckboxInput (attrs={'class':'filled-in'	}),
		}

class AreaForm(forms.Form):
	area= forms.ModelChoiceField(queryset = Area.objects.all(),empty_label=None)