from django.db import models
from carritos.models import Carrito
from productos.models import Producto

class DetalleCarro(models.Model):
    idDetalleC = models.AutoField(primary_key=True)
    idCarrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.idProducto.nombreP} - {self.cantidad}"