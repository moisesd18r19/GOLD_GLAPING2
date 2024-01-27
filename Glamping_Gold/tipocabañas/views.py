from django.shortcuts import render
from django.shortcuts import render, redirect
from tipocabañas.models import Tipocabaña

def tipocabañas(request):    
    tipocabañas_list = Tipocabaña.objects.all()    
    return render(request, 'tipocabañas/index.html', {'tipocabañas_list': tipocabañas_list})

def change_status_tipocabaña(request, tipocabaña_id):
    tipocabaña = Tipocabaña.objects.get(pk=tipocabaña_id)
    tipocabaña.status = not tipocabaña.status
    tipocabaña.save()
    return redirect('tipocabañas')

def tipocabañas(request):
    return render(request, 'tipocabañas/index.html')
# Create your views here.
