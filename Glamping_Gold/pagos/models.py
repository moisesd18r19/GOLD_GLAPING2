from django.db import models

class Pago(models.Model):
    fecha = models.DateField( default='True')
    metodo_pago = models.CharField(max_length=200)
    valor = models.IntegerField( default='True')
    status = models.BooleanField(default=True)
    reserva = models.ForeignKey('reservas.Reserva', on_delete= models.DO_NOTHING, default='True')
    
    def __str__(self):
        return self.reserva


    
    

    
# Create your models here.
