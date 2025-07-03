

from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        extra_kwargs = {
            'contraseña': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('contraseña', None)
        if password is not None:
            # Genera el hash seguro de la contraseña
            validated_data['contraseña'] = make_password(password)
        return super().create(validated_data)
