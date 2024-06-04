from rest_framework import serializers
from .models import Departamento, Empleado, PuestoTrabajo
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["id","nombre", "telefono", "created", "updated"]


class PuestoTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoTrabajo
        fields = ["id","nombre","created", "updated"]


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ["id","nombre","fecha_nacimiento","antiguedad","departamento","created", "updated"]
