from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Task


class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'fecha_vencimiento', 'is_complete']


admin.site.register(Task, TaskAdmin)