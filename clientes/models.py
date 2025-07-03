from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombreC = models.CharField(max_length=50)
    apellidoC = models.CharField(max_length=50)
    numeroTelefonico = models.CharField(max_length=15)
    usuario = models.CharField(max_length=20, unique=True)
    # Se cambia el campo de contraseña a un CharField para almacenar el hash (no en texto plano)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.nombreC