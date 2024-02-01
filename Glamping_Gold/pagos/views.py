from django.shortcuts import render, redirect
from .models import Pago
from .forms import  PagoForm


def pagos(request):    
    pagos_list = Pago.objects.all()    
    return render(request, 'pagos/index.html', {'pagos_list': pagos_list})

def change_status_pago(request, pago_id):
    pago = Pago.objects.get(pk=pago_id)
    pago.status = not pago.status
    pago.save()
    return redirect('pagos')


def create_pagos(request):
    form = PagoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pagos')    
    return render(request, 'pagos/create.html', {'form': form})

#