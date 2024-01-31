from django.shortcuts import render, redirect
from .models import Cabaña
from cabañas.forms import CabañaForm

def cabañas(request):    
    cabañas_list = Cabaña.objects.all()    
    return render(request, 'cabañas/index.html', {'cabañas_list': cabañas_list})

def change_status_cabaña(request, cabaña_id):
    cabaña = Cabaña.objects.get(pk=cabaña_id)
    cabaña.status = not cabaña.status
    cabaña.save()
    return redirect('cabañas')

def create_cabaña(request):
    form = CabañaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cabañas')    
    return render(request, 'cabañas/create.html', {'form': form})


# Create your views here.
