from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente  
from django.contrib import messages

def cliente(request):    
    cliente_list = Cliente.objects.all()  
    return render(request, 'cliente/index.html', {'cliente_list': cliente_list})

def change_status_cliente(request, cliente_id):
    cliente_instance = Cliente.objects.get(pk=cliente_id) 
    cliente_instance.status = not cliente_instance.status
    cliente_instance.save()
    return redirect('cliente')

def create_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente')    
    return render(request, 'cliente/create.html', {'form': form})

def delete_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    try:
        cliente.delete()        
        messages.success(request, 'Cliente eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el autor porque está asociado a un libro.')
    return redirect('cliente')