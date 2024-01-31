from django import forms
from . models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = "__all__"
        exclude = ['status']
        labels = {
            'fecha': 'Fecha',
            'metodo_pago': 'Metodo Pago',
            'valor': 'Valor',                      
        }
        widgets = {
            'fecha': forms.TextInput(attrs={'placeholder': 'Ingresa la fecha'}),
            'metodo_pago': forms.TextInput(attrs={'placeholder': 'Ingresa el metodo de pago'}),
            'valor': forms.MultiValueField(attrs={'placeholder': 'Ingresa el valor a pagar'}),            
        }