from rest_framework import viewsets
from .models import DetalleCarro
from .serializers import DetalleCarroSerializer


class DetalleCarroViewSet(viewsets.ModelViewSet):
    queryset = DetalleCarro.objects.all()
    serializer_class = DetalleCarroSerializer
