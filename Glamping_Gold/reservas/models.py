from django.db import models

class Reserva(models.Model):
    coder = models.CharField(max_length=255, default= True )
    fecha_reserva = models.DateField(default= True)
    fecha_inicio = models.DateField(default= True)
    fecha_fin = models.DateField(default= True)
    valor = models.IntegerField(default= True)
    cliente = models.ForeignKey('cliente.Cliente', on_delete= models.DO_NOTHING, default= True)

    def __str__(self):
        return self.coder
# Create your models here.
