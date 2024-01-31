from django.db import models


class Cabaña(models.Model):
    nombre= models.CharField(max_length=50)
    capacidad = models.IntegerField(max_length=10)
    precio = models.IntegerField(max_length=20)
    descripcion = models.CharField(max_length=250)
    imagen = models.FileField(upload_to='static/images_cabaña', null=True)
    status = models.BooleanField(default=True)
    tipo_cabaña = models.ForeignKey('tipocabañas.Tipocabaña', on_delete=models.DO_NOTHING)
    
    
    
    def __str__(self):
        return self.nombre 
    
    
# Create your models here.
