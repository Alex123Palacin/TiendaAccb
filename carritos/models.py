from django.db import models
from clientes.models import Cliente

class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.idCliente.usuario}"