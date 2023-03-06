from django.db import models

# Create your models here.

class Correo(models.Model):
    destinatario= models.CharField(max_length= 50)
    emisor= models.CharField(max_length= 50)
    fecha = models.DateField()
    empresa = models.CharField(max_length= 50) # a la que pertenece el emisor del correo, 
    codigoSMTP= models.CharField(max_length= 50) #único de correo por proveedor   (pos proveedor no manejamos)
    contenido= models.TextField(max_length= 200)