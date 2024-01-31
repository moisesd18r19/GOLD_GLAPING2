from django import forms
from . models import Cabaña

from cabañas.models import Cabaña

class CabañaForm(forms.ModelForm):
    cabaña = forms.ModelChoiceField(queryset=Cabaña.objects.filter(status=True).order_by('nombre'))
    class Meta:
        model = Cabaña
        fields = "__all__"
        exclude = ['status']
        labels = {
           'nombre' : 'Nombre',
           'capacidad' : 'Capacidad',
           'precio' : 'Precio',
           'descripcion' : 'Descripcion',
           'imagen' : 'Imagen',
           'tipo_cabaña' : 'Tipo_cabaña'
           
                                        
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'capacidad': forms.NumberInput(attrs={'placeholder': 'Ingresa capacidad'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingresa el precio'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingresa la descripción'}),  
            'imagen': forms.FileInput(attrs={'placeholder': 'Selecciona imagen'}), 
            'tipo_cabaña': forms.SelectMultiple(attrs={'placeholder': 'Ingrese tipo cabaña'})
        }