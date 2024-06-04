from django.contrib import admin
from .models import PedidoItem, Pedido


class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    raw_id_fields = ['producto']



@admin.register(PedidoItem)
class PedidoItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'producto', 'precio', 'cantidad']
    list_filter = ['id', 'pedido', 'producto', 'precio', 'cantidad', ]
    search_fields = ['id', 'cliente', 'pedido', 'producto', 'precio', 'cantidad', ]
    list_per_page = 8


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'user', 'nombre', 'apellidos', 'email', 'direccion', 'codigo_postal', 'ciudad',
                    'pais', 'created', 'updated']
    list_filter = ['pais', 'created', 'updated']
    search_fields = ['nombre', 'apellidos', 'email', 'direccion']
    inlines = [PedidoItemInline]
    readonly_fields = ['created', 'updated']
    list_per_page = 8
