from django.contrib import admin
from core.STORE.models import GaleriaProductos, Variante, Noticia
from core.STORE.models import Categoria, Producto


class GaleriaProductoInLine(admin.TabularInline):
    model = GaleriaProductos
    extra = 1


class VarianteAdmin(admin.ModelAdmin):
    list_display = ('producto', 'categoria_variante', 'valor', 'activo')
    list_editable = ('activo',)
    list_filter = ('producto', 'categoria_variante', 'valor', 'activo')


class VarianteInLine(admin.TabularInline):
    model = Variante
    extra = 1


@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_display = ['nombre', 'slug', 'descripcion']
    list_display_links = ('nombre',)
    list_filter = ( 'nombre',)
    prepopulated_fields = {'slug': ('nombre',)}
    list_per_page = 8


@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre','categoria', 'descripcion', 'color' ,'precio', 'stock' , 'disponibilidad', 'imagen_tag')
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [GaleriaProductoInLine, VarianteInLine]
    list_filter = ['nombre', 'categoria','color','precio', 'stock','disponibilidad']
    list_editable = ['precio', 'stock', 'disponibilidad']
    search_fields = ['nombre', 'categoria','color','precio', 'stock', 'disponibilidad',]
    list_display_links = ['nombre',]
    ordering = ['nombre', 'id']
    list_per_page = 8


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    list_per_page = 8




# admin.site.register(AddOpnion)

admin.site.register(GaleriaProductos)
admin.site.register(Variante, VarianteAdmin)
