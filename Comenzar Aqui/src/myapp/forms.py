from django import forms
from .models import ComprarArticulo


class CompraModelForm(forms.ModelForm):
	class Meta: 
		model = ComprarArticulo
		fields = ["nombre", "color", "tipo_de_comida", "receta"]
		widgets = {
    		'receta': forms.Textarea()
			}

def clean(self, *args, **kwargs):
	cleaned_data = super(CompraModelForm, self).clean(*args, **kwargs)
