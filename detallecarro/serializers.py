from rest_framework import serializers
from .models import DetalleCarro


class DetalleCarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCarro
        fields = '__all__'
