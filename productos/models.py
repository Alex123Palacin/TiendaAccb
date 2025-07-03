
from django.db import models

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreP = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    descripcion = models.TextField(default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagenP = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombreP
