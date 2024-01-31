from django.db import models

class Pago(models.Model):
    fecha = models.CharField(max_length=255)
    metodo_pago = models.CharField(max_length=200)
    valor = models.IntegerField(max_length=20)
    status = models.BooleanField(default=True)
    reserva = models.ForeignKey('reservas.reserva', on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.name
# Create your models here.
