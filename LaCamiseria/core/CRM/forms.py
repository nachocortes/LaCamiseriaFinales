from django import forms
from core.CRM.models import Cliente
from core.RRHH.models import Empleado


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar el queryset del campo comercial
        self.fields['comercial'].queryset = Empleado.objects.filter(puestoTrabajo__nombre='TecGestionComercial')