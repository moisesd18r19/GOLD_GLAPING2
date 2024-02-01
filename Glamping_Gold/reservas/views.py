from django.shortcuts import render, redirect
from .models import Reserva
from reservas.forms import ReservaForm

def reservas(request):    
    reservas_list = Reserva.objects.all()    
    return render(request, 'reservas/index.html', {'reservas_list': reservas_list})



def create_reserva(request):
    form = ReservaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('reservas')    
    return render(request, 'reservas/create.html', {'form': form})

# Create your views here.
