from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Reserva

def reservas(request):    
    reservas_list = Reserva.objects.all()    
    return render(request, 'reservas/index.html', {'reservas_list': reservas_list})

def change_status_reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    reserva.status = not reserva.status
    reserva.save()
    return redirect('reservas')
# Create your views here.
