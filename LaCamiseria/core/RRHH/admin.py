from django.contrib import admin
from .models import Departamento, PuestoTrabajo, Empleado


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'telefono', 'responsable', 'id')
    ordering = ('nombre', 'id')
    search_fields = ('nombre', 'telefono','responsable')
    list_display_links = ('nombre',)
    list_filter = ('nombre','responsable', "telefono")
    list_per_page = 8


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('apellidos', 'nombre')
    list_display = ('imagen_tag', 'empleado', 'dni', 'email', 'departamento', 'puestoTrabajo','fecha_nacimiento','antiguedad', 'id')
    search_fields = ('empleado', 'dni', 'email', 'departamento', 'puestoTrabajo','fecha_nacimiento','antiguedad', 'id')
    list_display_links = ('empleado','departamento','puestoTrabajo')
    list_filter = ( 'apellidos', 'nombre', 'dni', 'departamento','puestoTrabajo', 'antiguedad')
    list_per_page = 8


@admin.register(PuestoTrabajo)
class PuestoTrabajoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'departamento')
    ordering = ('departamento', 'nombre')
    search_fields = ('nombre','departamento')
    list_display_links = ('nombre',)
    list_filter = ('nombre','departamento')
    list_per_page = 8
