from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from core.CRM.forms import ClienteForm
from core.CRM.models import Direccion, Cliente
from core.RRHH.models import Empleado
from core.VENTAS.models import Pedido


class ClenteResource(resources.ModelResource):
    class Meta:
        model = Cliente


class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1
    fields = ['tipoDireccion', 'tipoVia', 'calle', 'numero', 'codigoPostal', 'ciudad', 'pais']
    readonly_fields = ['tipoDireccion', 'tipoVia', 'calle', 'numero', 'codigoPostal', 'ciudad', 'pais']


class PedidoInline(admin.TabularInline):
    model = Pedido
    extra = 1
    fields = ['telefono', 'email', 'created']
    readonly_fields = ['telefono', 'email', 'created']


class ComercialTecGestionFilter(admin.SimpleListFilter):
    title = 'Comercial'
    parameter_name = 'comercial'

    def lookups(self, request, model_admin):
        empleados = Empleado.objects.filter(puestoTrabajo__nombre='TecGestionComercial')
        return [(e.id, e.nombre) for e in empleados]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(comercial__id=self.value())


@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = ClienteForm
    list_display = (
        'nombre', 'documento', 'user', 'get_comercial', 'email', 'telefono', 'tipoCliente',)
    inlines = [PedidoInline, DireccionInline]
    list_filter = ('nombre', 'tipoCliente', 'telefono', 'email', ComercialTecGestionFilter,)
    search_fields = ('nombre', 'documento', 'email', 'telefono', ComercialTecGestionFilter)
    readonly_fields = ('created', 'updated')
    resource_class = ClenteResource
    list_per_page = 8

    def get_comercial(self, obj):
        return obj.comercial.nombre if obj.comercial else 'No asignado'

    get_comercial.short_description = 'Comercial'


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipoDireccion', 'tipoVia', 'calle', 'numero', 'codigoPostal', 'ciudad', 'pais')
    list_filter = ('cliente', 'tipoDireccion', 'telefono', 'codigoPostal', 'ciudad', 'pais',)
    search_fields = ('calle', 'numero', 'codigoPostal', 'ciudad', 'pais')
    readonly_fields = ('created', 'updated')
    list_per_page = 8
