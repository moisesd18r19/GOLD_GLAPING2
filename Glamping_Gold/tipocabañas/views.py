from django.shortcuts import render
from django.shortcuts import render, redirect
from tipocabañas.models import Tipocabaña
from .forms import TipocabañaForm
from django.contrib import messages
from django.http import JsonResponse

def tipocabañas(request):    
    tipocabañas_list = Tipocabaña.objects.all()    
    return render(request, 'tipocabañas/index.html', {'tipocabañas_list': tipocabañas_list})

def change_status_tipocabaña(request, tipocabaña_id):
    tipocabaña = Tipocabaña.objects.get(pk=tipocabaña_id)
    tipocabaña.status = not tipocabaña.status
    tipocabaña.save()
    return redirect('tipocabañas')

def create_tipocabaña(request):
    form = TipocabañaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tipocabañas')    
    return render(request, 'tipocabañas/create.html', {'form': form})

def detail_tipocabaña(request, tipocabaña_id):
    tipocabaña = Tipocabaña.objects.get(pk=tipocabaña_id)
    data = { 'nombre': tipocabaña.nombre }
    return JsonResponse(data)


def delete_tipocabaña(request, tipocabaña_id):
    tipocabaña = Tipocabaña.objects.get(pk=tipocabaña_id)
    try:
        tipocabaña.delete()        
        messages.success(request, 'Tipo de cabaña eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el Tipo de cabaña porque está asociado a un libro.')
    return redirect('tipocabañas')





