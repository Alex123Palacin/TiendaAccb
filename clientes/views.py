from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteLoginAPIView(APIView):
    """
    Vista para iniciar sesión.
    Recibe una petición POST con un JSON que contenga:
      - "usuario": el nombre de usuario.
      - "password": la contraseña en texto plano.
    Busca al cliente y utiliza check_password() para validar la contraseña.
    """
    def post(self, request, *args, **kwargs):
        usuario = request.data.get('usuario')
        password = request.data.get('password')

        if not usuario or not password:
            return Response(
                {"detail": "Se requieren 'usuario' y 'password'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cliente = Cliente.objects.get(usuario=usuario)
        except Cliente.DoesNotExist:
            return Response(
                {"detail": "Usuario no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        if check_password(password, cliente.contraseña):
            return Response(
                {"detail": "Inicio de sesión exitoso."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Contraseña incorrecta."},
                status=status.HTTP_400_BAD_REQUEST
            )